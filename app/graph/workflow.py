from langgraph.graph import StateGraph, START, END

from .state import HotelState
from .nodes import (
    classify_question,
    retrieve_documents,
    booking_node,
    restaurant_node,
    generate_answer,
)

builder = StateGraph(HotelState)

builder.add_node("classifier", classify_question)
builder.add_node("retriever", retrieve_documents)
builder.add_node("generator", generate_answer)
builder.add_node("booking", booking_node)
builder.add_node("restaurant", restaurant_node)


builder.add_edge(START, "classifier")

def route(state):

    if state["intent"] == "booking":
        return "booking"

    if state["intent"] == "restaurant":
        return "restaurant"

    return "retriever"

builder.add_conditional_edges(
    "classifier",
    route,
    {
        "booking": "booking",
        "restaurant": "restaurant",
        "retriever": "retriever",
    },
)

builder.add_edge("retriever", "generator")
builder.add_edge("generator", END)
builder.add_edge("booking", END)
builder.add_edge("restaurant", END)


hotel_graph = builder.compile()