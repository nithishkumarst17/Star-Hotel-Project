from app.graph.state import HotelState
from app.services.embedding_service import EmbeddingService
from app.services.retriever import RetrieverService
from app.services.prompt import hotel_prompt
from app.services.llm_service import SarvamLLM


def classify_question(state: HotelState):

    question = state["question"].lower()

    if any(word in question for word in ["book", "booking", "reserve"]):
        intent = "booking"
    elif any(word in question for word in ["restaurant", "food", "menu"]):
        intent = "restaurant"
    elif any(word in question for word in ["pool", "wifi", "spa", "room", "check", "hotel"]):
        intent = "hotel_info"
    else:
        intent = "general"
    return {
        "intent": intent
    }

def retrieve_documents(state: HotelState):

    embedding = EmbeddingService().get_embedding_model()

    retriever = RetrieverService(
        embedding
    ).get_retriever()

    docs = retriever.invoke(
        state["question"]
    )

    context = "\n\n".join(
        [
            doc.page_content
            for doc in docs
        ]
    )

    return {
        "retrieved_docs": docs,
        "context": context
    }

def build_prompt(state: HotelState):
    prompt = hotel_prompt.format(
        context=state["context"],
        question=state["question"]
    )

    return {
        "prompt": prompt
    }

def generate_answer(state: HotelState):
    llm = SarvamLLM()
    answer = llm.invoke(
        state["prompt"]
    )
    return {
        "answer": answer
    }