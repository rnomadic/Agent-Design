'''
Problem 2: Design a RAGSystem Class 
o	Create a RAGSystem class that takes a RetrievalStrategy and an LLM as dependencies.
o	Implement methods for retrieve_context() and generate_response().
o	This emphasizes composition and dependency injection, promoting modular design.


Composition: The RAGSystem class is composed of two other objects: RetrievalStrategy and LLM. 
It doesn't inherit from them; it has-a relationship with them. This allows for flexibility in 
choosing and combining different retrieval methods and LLMs.

Dependency Injection: 
By decoupling the creation of dependent objects from the class that uses them, 
we achieve a more modular and cohesive design. DI aligns closely with the object-oriented design 
principle of “Inversion of Control” (IoC), which shifts control of object creation and binding 
from the class itself to an external entity. To understand DI go to below 1 min video.

https://www.youtube.com/shorts/-rf_wzK6vPU

Dependency injection can be implemented in various ways, with constructor and method injection being the most prevalent. 
Constructor injection involves providing dependencies through a class’s constructor. 
It’s a straightforward method that ensures a class has all its necessary dependencies before use. 

The RAGSystem class receives its dependencies (RetrievalStrategy and LLM) 
through its constructor. This is a key aspect of dependency injection. Instead of creating these 
dependencies itself, the RAGSystem is given pre-existing instances. This promotes loose coupling, 
making the code easier to test, maintain, and extend.

Abstraction: The use of abstract base classes (RetrievalStrategy and LLM) defines a contract for how 
retrieval and LLM components should behave. This allows for different concrete implementations to be 
used interchangeably, as long as they adhere to the interface.

'''
from abc import ABC, abstractmethod

class RetrievalStrategy(ABC):
    """
    Abstract base class for retrieval strategies.
    """
    @abstractmethod
    def retrieve(self, query: str) -> list:
        """
        Retrieves relevant information based on the query.
        """
        pass

class LLM(ABC):
    """
    Abstract base class for Large Language Models.
    """
    @abstractmethod
    def generate_response(self, context: str, query: str) -> str:
        """
        Generates a response based on the context and query.
        """
        pass

class RAGSystem:
    """
    Implements a Retrieval Augmented Generation (RAG) system.
    """

    def __init__(self, retrieval_strategy: RetrievalStrategy, llm: LLM):
        """
        Initializes the RAGSystem with a retrieval strategy and an LLM.
        """
        self.retrieval_strategy = retrieval_strategy
        self.llm = llm

    def retrieve_context(self, query: str) -> list:
        """
        Retrieves relevant context using the retrieval strategy.
        """
        return self.retrieval_strategy.retrieve(query)

    def generate_response(self, query: str) -> str:
        """
        Generates a response using the LLM, augmented with retrieved context.
        """
        context = self.retrieve_context(query)
        if context:
            context_str = " ".join(context)  # Combine context into a single string
            return self.llm.generate_response(context_str, query)
        else:
            return self.llm.generate_response("", query)  # Or handle no context scenario


#############################################################################################

# Concrete Implementations (for demonstration)
class SimpleRetrieval(RetrievalStrategy):
    """
    A simple retrieval strategy for demonstration purposes.
    """
    def __init__(self, data):
      self.data = data

    def retrieve(self, query: str) -> list:
        """
        Retrieves from a predefined dictionary.
        """
        print(f"Simple Retrieval: Retrieving context for '{query}'")
        return self.data.get(query,)

class SimpleLLM(LLM):
    """
    A simple LLM for demonstration purposes.
    """
    def generate_response(self, context: str, query: str) -> str:
        """
        Generates a simple response.
        """
        print(f"Simple LLM: Generating response for '{query}' with context: '{context}'")
        return f"Response: '{query}' with context: '{context}'"

# Example Usage:
if __name__ == "__main__":
    # Create a SimpleRetrieval instance with some data
    data = {
        "What is AI?": ["AI is artificial intelligence.", "It involves creating intelligent machines."],
        "RAG explanation": ["RAG stands for Retrieval Augmented Generation.", "It combines retrieval and generation."]
    }
    retrieval = SimpleRetrieval(data)

    # Create a SimpleLLM instance
    llm_model = SimpleLLM()

    # Create a RAGSystem with the concrete implementations
    rag_system = RAGSystem(retrieval, llm_model)

    # Example usage
    query = "Explain RAG"
    response = rag_system.generate_response(query)
    print("RAG System Response:", response)

