"""Provider-agnostic Anthropic-compatible client factory.

Two providers are supported, switched by ``EXPOUND_PROVIDER``:

  anthropic (default)  → direct Anthropic API; uses ANTHROPIC_API_KEY.
  deepseek             → DeepSeek's Anthropic-compatible endpoint at
                         https://api.deepseek.com/anthropic; uses DEEPSEEK_API_KEY.

The factory also maps logical roles ("orchestrator" / "sub_agent" / "fast")
to provider-specific model names so callers don't hard-code Claude model IDs.

Per-role overrides via env: ``EXPOUND_MODEL_ORCHESTRATOR`` etc.
"""

from __future__ import annotations

import json
import os
import re
from typing import Any, Literal, TypeVar

import anthropic
from pydantic import BaseModel

Provider = Literal["anthropic", "deepseek"]
Role = Literal["orchestrator", "sub_agent", "fast"]

T = TypeVar("T", bound=BaseModel)

_VALID_PROVIDERS = ("anthropic", "deepseek")

_MODEL_TABLE: dict[str, dict[str, str]] = {
    "anthropic": {
        "orchestrator": "claude-opus-4-7",
        "sub_agent": "claude-sonnet-4-6",
        "fast": "claude-haiku-4-5",
    },
    "deepseek": {
        "orchestrator": "deepseek-reasoner",
        "sub_agent": "deepseek-chat",
        "fast": "deepseek-chat",
    },
}


def get_provider() -> Provider:
    p = os.environ.get("EXPOUND_PROVIDER", "anthropic").lower()
    if p not in _VALID_PROVIDERS:
        raise ValueError(
            f"EXPOUND_PROVIDER={p!r} is not supported. "
            f"Use one of: {', '.join(_VALID_PROVIDERS)}"
        )
    return p  # type: ignore[return-value]


def get_model(role: Role) -> str:
    override = os.environ.get(f"EXPOUND_MODEL_{role.upper()}")
    if override:
        return override
    return _MODEL_TABLE[get_provider()][role]


def make_client() -> anthropic.Anthropic:
    provider = get_provider()
    if provider == "anthropic":
        return anthropic.Anthropic()
    if provider == "deepseek":
        api_key = os.environ.get("DEEPSEEK_API_KEY")
        if not api_key:
            raise RuntimeError(
                "EXPOUND_PROVIDER=deepseek requires DEEPSEEK_API_KEY to be set."
            )
        return anthropic.Anthropic(
            api_key=api_key,
            base_url="https://api.deepseek.com/anthropic",
        )
    raise AssertionError(f"unreachable provider: {provider}")


def supports_anthropic_betas() -> bool:
    """True only on the native Anthropic endpoint.

    Beta features (``client.beta.messages.tool_runner``, ``thinking={...}``,
    explicit ``cache_control``, ``anthropic-beta`` headers) are silently
    ignored or 4xx-rejected on third-party Anthropic-compat shims like
    DeepSeek's. Callers gate optional kwargs on this.
    """
    return get_provider() == "anthropic"


def thinking_kwargs() -> dict:
    """Adaptive-thinking kwargs only when on native Anthropic; else empty."""
    if supports_anthropic_betas():
        return {"thinking": {"type": "adaptive"}}
    return {}


def required_env_var() -> str:
    return "ANTHROPIC_API_KEY" if get_provider() == "anthropic" else "DEEPSEEK_API_KEY"


_FENCE_RE = re.compile(r"^```(?:json)?\s*\n?(.*?)\n?```\s*$", re.DOTALL)


def _strip_json_fence(text: str) -> str:
    s = text.strip()
    m = _FENCE_RE.match(s)
    return m.group(1).strip() if m else s


def parse_message(
    client: anthropic.Anthropic,
    *,
    output_format: type[T],
    system: Any,
    messages: list[dict],
    model: str,
    max_tokens: int,
    **extra_kwargs: Any,
) -> T:
    """Provider-aware structured-output parsing → validated Pydantic model.

    On Anthropic: uses native ``messages.parse`` (server-enforced schema via
    tool protocol). On DeepSeek's Anthropic-compat shim: that protocol isn't
    implemented, so we ask for JSON in the system prompt, call ``messages.create``,
    strip a possible markdown fence, and validate locally.
    """
    if supports_anthropic_betas():
        response = client.messages.parse(
            model=model,
            max_tokens=max_tokens,
            system=system,
            messages=messages,
            output_format=output_format,
            **extra_kwargs,
        )
        if response.parsed_output is None:
            raise RuntimeError(
                f"structured parse returned None (stop_reason={response.stop_reason})"
            )
        return response.parsed_output

    schema_json = json.dumps(output_format.model_json_schema(), ensure_ascii=False)
    json_directive = (
        "Respond with a SINGLE JSON object that conforms EXACTLY to this JSON Schema. "
        "Rules:\n"
        "  - Do NOT wrap in markdown code fences.\n"
        "  - Do NOT include any commentary, prefix, or suffix text.\n"
        "  - For enum fields you MUST use one of the listed values verbatim — "
        "never null, 'None', 'N/A', 'unknown', or any other substitute. "
        "If you are unsure, pick the most conservative valid enum value.\n"
        "  - All required fields must be present.\n\n"
        f"Schema:\n{schema_json}"
    )

    if isinstance(system, list):
        system_compat = list(system) + [{"type": "text", "text": json_directive}]
    elif isinstance(system, str):
        system_compat = system + "\n\n" + json_directive
    else:
        system_compat = json_directive

    convo = list(messages)
    last_error: Exception | None = None
    for attempt in range(2):
        response = client.messages.create(
            model=model,
            max_tokens=max_tokens,
            system=system_compat,
            messages=convo,
            **extra_kwargs,
        )
        text_blocks = [
            b.text for b in response.content if getattr(b, "type", None) == "text"
        ]
        if not text_blocks:
            raise RuntimeError(
                f"no text content in response (stop_reason={response.stop_reason})"
            )
        raw = "\n".join(text_blocks)
        cleaned = _strip_json_fence(raw)
        try:
            return output_format.model_validate_json(cleaned)
        except Exception as e:
            last_error = e
            if attempt == 0:
                convo = convo + [
                    {"role": "assistant", "content": raw},
                    {
                        "role": "user",
                        "content": (
                            "Your previous response failed schema validation. "
                            f"Error: {e}\n\nReturn a corrected JSON object following all "
                            "rules. Pay special attention to enum fields — use only the "
                            "listed values."
                        ),
                    },
                ]
                continue
            raise RuntimeError(
                f"structured parse failed after retry: {e}\n--- raw model output ---\n{raw}"
            ) from e
    raise AssertionError("unreachable") from last_error
