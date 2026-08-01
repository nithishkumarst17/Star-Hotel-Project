from typing import TypedDict, List
from langchain_core.documents import Document


class HotelState(TypedDict):
    question: str
    intent: str
    retrieved_docs: List[Document]
    context: str
    prompt: str
    answer: str