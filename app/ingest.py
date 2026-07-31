from app.services.document_loader import DocumentLoader
from app.services.text_splitter import TextSplitter
from app.services.embedding_service import EmbeddingService
from app.services.vector_store import VectorStoreService

def main():
    loader = DocumentLoader()
    documents = loader.load_documents()
    print(f"Pages loaded: {len(documents)}")
    splitter = TextSplitter()
    chunks = splitter.split_documents(documents)
    print(f"Chunks created: {len(chunks)}")

    embedding_service = EmbeddingService()
    embedding_model = embedding_service.get_embedding_model()

    vector_service = VectorStoreService(
        embedding_model
    )
    vector_service.create_vector_db(chunks)
    print("Vector DB created successfully")

if __name__ == "__main__":
    main()