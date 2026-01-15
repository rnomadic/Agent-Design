from abc import ABC, abstractmethod #implement Abstract Base Classes (ABCs)
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# 1. Define the RetrievalStrategy Interface, abstract base class
class RetrievalStrategy(ABC):
    """
    Abstract interface for different retrieval strategies.
    """
    @abstractmethod
    def retrieve_topk(self, query: str, data: list, k:int) -> list:
        """
        Retrieves relevant items from the data based on the query.

        Args:
            query: The search query (str).
            data: The list of items to search within (list of str).

        Returns:
            A list of relevant items (list of str).
        """
        pass

# 2. Implement Concrete Strategies
class KeywordSearchStrategy(RetrievalStrategy):
    """
    Retrieves items based on keyword matching.
    """
    def retrieve_topk(self, query: str, data: list, k:int) -> list:
        """
        Simple keyword-based retrieval.

        Args:
            query: The search query (str).
            data: The list of documents to search within (list of str).

        Returns:
            A list of documents containing the query keywords (list of str).
        """
        relevant_items = [item for item in data if query.lower() in item.lower()]
        print(f"Keyword Search: Retrieved '{relevant_items}' for query '{query}'")
        return relevant_items

class VectorSearchStrategy(RetrievalStrategy):
    """
    Retrieves items based on vector similarity using TF-IDF and cosine similarity.
    """
    def __init__(self):
        self.vectorizer = TfidfVectorizer()

    def retrieve_topk(self, query: str, data: list, k:int) -> list:
        """
        Retrieves items using TF-IDF vectorization and cosine similarity.

        Args:
            query: The search query (str).
            data: The list of documents to search within (list of str).

        Returns:
            A list of documents ranked by similarity to the query (list of str).
        """
        vectors = self.vectorizer.fit_transform(data + [query])  # Vectorize data and query
        query_vector = vectors[-1]  # Vector for the query
        data_vectors = vectors[:-1]   # Vectors for the data

        similarities = cosine_similarity(query_vector, data_vectors)[0] # Calculate cosine similarity
        
        # Rank documents by similarity
        # [::-1] reverses the sorted array, effectively giving you the indices that sort the similarities array in descending order.
        ranked_indices = np.argsort(similarities)[::-1][:k] #return top k element
        ranked_items = [data[i] for i in ranked_indices]
        print(f"Vector Search: Retrieved '{ranked_items}' for query '{query}'")
        return ranked_items

# 3. Example Usage
if __name__ == "__main__":
    data = [
        "The quick brown fox jumps over the lazy dog",
        "A fast brown rabbit hops across the field",
        "The dog is lazy",
        "Brown foxes are quick"
    ]

    query = "quick brown"

    # Use Keyword Search
    k=2
    keyword_search = KeywordSearchStrategy()
    keyword_results = keyword_search.retrieve_topk(query, data,k)
    print("Keyword Search Results:", keyword_results)

    # Use Vector Search
    vector_search = VectorSearchStrategy()
    vector_results = vector_search.retrieve_topk(query, data,k)
    print("Vector Search Results:", vector_results)