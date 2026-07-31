from typing import TypedDict, List
class HotelState(TypedDict):
    question: str
    intent: str
    context: str
    answer: str
    retrieved_docs: List[str]