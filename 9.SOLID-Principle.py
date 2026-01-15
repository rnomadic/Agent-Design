from abc import ABC, abstractmethod

######################################################################################################
# 1. Single Responsibility Principle (SRP) - Separate classes for retrieval, reranking, and generation
######################################################################################################
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


#######################################################################################
# 2. Open/Closed Principle (OCP) - Extend functionality without modifying existing code
# Code should be Open for extension but closed for modification
#######################################################################################
class BM25Retriever(Retriever):
    def retrieve_documents(self, query: str):
        return ["Doc1", "Doc2"]

class NeuralReranker(Reranker):
    def rerank_documents(self, documents: list, query: str):
        return sorted(documents, key=lambda doc: len(doc), reverse=True)

class GPTGenerator(Generator):
    def generate_response(self, query: str, context: list):
        return f"Generated response based on: {context}"

###############################################################################
# 3. Liskov Substitution Principle (LSP) - Subtypes can be used interchangeably
###############################################################################
retriever: Retriever = BM25Retriever()
reranker: Reranker = NeuralReranker()
generator: Generator = GPTGenerator()

#################################################################################
# 4. Interface Segregation Principle (ISP) - No unnecessary methods in interfaces
# Dependency Injection - all the dependency passed through constructor
#################################################################################
class RAGPipeline:
    def __init__(self, retriever: Retriever, reranker: Reranker, generator: Generator):
        self.retriever = retriever
        self.reranker = reranker
        self.generator = generator
    
    def process_query(self, query: str):
        docs = self.retriever.retrieve_documents(query)
        reranked_docs = self.reranker.rerank_documents(docs, query)
        response = self.generator.generate_response(query, reranked_docs)
        return response

################################################################################################
# 5. Dependency Inversion Principle (DIP) - Depend on abstractions, not concrete implementations
################################################################################################
pipeline = RAGPipeline(retriever, reranker, generator)
response = pipeline.process_query("What is SOLID in AI?")
print(response)

