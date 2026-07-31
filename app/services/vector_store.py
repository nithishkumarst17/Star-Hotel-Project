from langchain_chroma import Chroma

class VectorStoreService:
    def __init__(self, embedding_model):
        self.embedding_model = embedding_model

    def create_vector_db(self, chunks):
        vector_db = Chroma.from_documents(
            documents=chunks,
            embedding=self.embedding_model,
            persist_directory="vector_db"
        )

        return vector_db