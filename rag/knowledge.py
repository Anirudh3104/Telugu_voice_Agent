"""Build Telugu knowledge text for RAG (one paragraph per scheme).

This module exposes a single function `build_scheme_knowledge(schemes)` that
returns a list of knowledge chunks. Avoids running work at import time so the
module is safe to import from other parts of the project.
"""

from typing import Any, Dict, List


def build_scheme_knowledge(schemes: List[Dict[str, Any]]) -> List[Dict[str, str]]:
    """Convert a list of scheme dicts into RAG-friendly Telugu text chunks.

    Args:
        schemes: list of scheme dictionaries (see `data/scheme.py` structure).

    Returns:
        A list of dictionaries with keys `scheme_id` and `text`.
    """

    scheme_knowledge: List[Dict[str, str]] = []

    for scheme in schemes:
        text = f"""
పథకం పేరు: {scheme.get('scheme_name')}
లాభాలు: {scheme.get('benefits')}

అర్హతలు:
"""

        eligibility = scheme.get("eligibility", {})
        for key, value in eligibility.items():
            text += f"- {key}: {value}\n"

        text += "\nదరఖాస్తు విధానం:\n"
        for step in scheme.get("apply_steps", []):
            text += f"- {step}\n"

        text += "\nఅవసరమైన పత్రాలు:\n"
        for doc in scheme.get("required_documents", []):
            text += f"- {doc}\n"

        scheme_knowledge.append({
            "scheme_id": scheme.get("scheme_id", ""),
            "text": text.strip(),
        })

    return scheme_knowledge


if __name__ == "__main__":
    # If run as a script, try to import schemes and print the number of chunks.
    try:
        from data.scheme import schemes  # type: ignore
    except Exception as exc:  # pragma: no cover - runtime guard
        print("Could not import 'schemes' from data.scheme:", exc)
        schemes = []

    chunks = build_scheme_knowledge(schemes)
    print("RAG knowledge chunks created:", len(chunks))
