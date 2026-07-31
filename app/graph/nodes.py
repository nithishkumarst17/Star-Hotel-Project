from typing import Dict

def classify_question(state) -> Dict:
    question = state["question"].lower()
    if any(word in question for word in ["book", "booking", "reserve"]):
        intent = "booking"
    elif any(word in question for word in ["restaurant", "food", "menu"]):
        intent = "restaurant"
    else:
        intent = "hotel_info"
    return {
        "intent": intent
    }

def retrieve_documents(state):
    question = state["question"]
    docs = [
        "Hotel has rooftop swimming pool.",
        "Check-in starts at 2 PM.",
        "Breakfast is from 7 AM to 10 AM."
    ]

    context = "\n".join(docs)
    return {
        "retrieved_docs": docs,
        "context": context
    }

def booking_node(state):
    return {
        "answer": "Booking module will be implemented later."
    }

def restaurant_node(state):
    return {
        "answer": "Restaurant information module will be implemented later."
    }

def generate_answer(state):
    prompt = f"""
You are a Hotel AI Assistant.
Answer ONLY using the context.

Context:
{state['context']}

Question:
{state['question']}
"""
    answer = f"Mock Answer:\n{prompt}"
    return {
        "answer": answer
    }