from langchain_core.prompts import PromptTemplate

hotel_prompt = PromptTemplate(
    template="""
You are a 5 star hotel AI assistant.
Answer the question only using the context.
If the answer is not available in the context,
say:
"I don't have this information."
Context:

{context}
Question:
{question}
Answer:
""",
    input_variables=[
        "context",
        "question"
    ]
)