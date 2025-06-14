import os
import chromadb
from chromadb.utils import embedding_functions
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class ChromaDBService:
    def __init__(self, path=None, collection_name=None):
        # Use environment variables or defaults
        self.db_path = path or os.getenv("CHROMA_DB_PATH", "db/chroma_db")
        self.collection_name = collection_name or os.getenv("CHROMA_COLLECTION_NAME", "financial_reports")
        self.client = chromadb.PersistentClient(path=self.db_path)
        self.embedding_function = embedding_functions.SentenceTransformerEmbeddingFunction(model_name="all-MiniLM-L6-v2")
        self.collection = self.client.get_or_create_collection(
            name=self.collection_name,
            embedding_function=self.embedding_function
        )

    def query(self, query_text: str, n_results: int = 3) -> list:
        try:
            results = self.collection.query(query_texts=[query_text], n_results=n_results)
            return results.get('documents', [[]])[0]
        except Exception as e:
            return [f"Error querying knowledge base: {e}"]

    def populate_db_if_empty(self):
        if self.collection.count() == 0:
            docs = [
                "NVIDIA's Q1 2025 earnings exceeded expectations, driven by strong demand for its H100 GPUs in the data center segment.",
                "AMD announced its new MI400 accelerator, positioning it as a direct competitor to NVIDIA's Blackwell architecture.",
                "Market sentiment for the semiconductor industry remains bullish, though concerns about supply chain stability persist."
            ]
            ids = ["doc1", "doc2", "doc3"]
            self.collection.add(documents=docs, ids=ids)
            print("Knowledge base populated with initial documents.") 