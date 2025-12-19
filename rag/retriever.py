from typing import List, Dict


def retrieve_scheme_info(
    scheme_id: str,
    scheme_knowledge: List[Dict[str, str]]
) -> str:
    """
    Constrained RAG retrieval:
    Returns Telugu knowledge text for the selected scheme only.

    Args:
        scheme_id: ID of the selected scheme
        scheme_knowledge: List of RAG knowledge chunks

    Returns:
        Telugu text describing the scheme
    """

    for item in scheme_knowledge:
        if item.get("scheme_id") == scheme_id:
            return item.get("text", "")

    return "సంబంధిత సమాచారం లభించలేదు."
