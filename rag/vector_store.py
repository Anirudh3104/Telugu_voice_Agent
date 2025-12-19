from typing import List, Dict, Tuple

import faiss
import numpy as np
from sentence_transformers import SentenceTransformer


def build_faiss_index(
    scheme_knowledge: List[Dict[str, str]]
) -> Tuple[faiss.IndexFlatL2, SentenceTransformer]:
    """
    Build FAISS vector index for Telugu scheme knowledge.

    Args:
        scheme_knowledge: List of RAG knowledge chunks

    Returns:
        FAISS index and embedding model
    """

    # Load multilingual embedding model (supports Telugu)
    embedding_model = SentenceTransformer(
        "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
    )

    # Prepare texts
    texts = [item["text"] for item in scheme_knowledge]

    # Generate embeddings
    embeddings = embedding_model.encode(texts, show_progress_bar=True)

    # Create FAISS index
    dimension = embeddings.shape[1]
    index = faiss.IndexFlatL2(dimension)
    index.add(np.array(embeddings))

    return index, embedding_model
