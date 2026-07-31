from langchain_chroma import Chroma

class RetrieverService:
    def __init__(self, embedding_model):
        self.vector_db = Chroma(
            persist_directory="vector_db",
            embedding_function=embedding_model
        )

    def get_retriever(self):
        retriever = self.vector_db.as_retriever(
            search_type="similarity",
            search_kwargs={
                "k": 5
            }
        )

        return retriever