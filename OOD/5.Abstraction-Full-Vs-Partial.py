from abc import ABC, abstractmethod

# Full Abstraction (Interface-like behavior)
class Retriever(ABC):
    @abstractmethod
    def retrieve_documents(self, query: str):
        pass

class Reranker(ABC):
    @abstractmethod
    def rerank_documents(self, documents: list, query: str):
        pass

class Generator(ABC):
    @abstractmethod
    def generate_response(self, query: str, context: list):
        pass

#Partial Abstraction
class SampleRetriever(Retriever):
    def retrieve_documents(self, query: str):
        print(f"Retrieving documents for query: {query}")
        return ["Document 1", "Document 2"]
    
class SampleGenerator(Generator):
    def generate_response(self, query: str, context: list):
        print(f"Generating response based on context: {context}")
        return "Generated response based on retrieved documents."
    
#Implement RAG system class
class RAGSystem:
    def __init__(self, retriever: Retriever, generator: Generator):
        self.retriever = retriever
        self.generator = generator

    def process_entry(self, query :  str):
        docs = self.retriever.retrieve_documents(query)
        response = self.generator.generate_response(docs)
        return response
    
#Demonstration
retriever = SampleRetriever()
generator = SampleGenerator()

rag_system = RAGSystem(retriever, generator)
query = "What is data abstraction?"
response = rag_system.process_entry(query)
print(response)


