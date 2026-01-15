'''
Problem 4: Create a Simple Factory for Agents (Factory Pattern) 
o	Design an AgentFactory class that creates different types of agents based on input.
o	This demonstrates the Factory pattern, simplifying object creation.

''' 
from abc import ABC, abstractmethod

class Agent(ABC):
    """
    Abstract base class for AI agents.
    """
    @abstractmethod
    def process(self, input_data):
        """
        Processes the input data.
        """
        pass

class RetrievalAgent(Agent):
    """
    Concrete agent class for retrieving information.
    """
    def process(self, input_data):
        """
        Retrieves information based on the input.
        """
        print(f"RetrievalAgent processing: {input_data}")
        # ... (Implementation for retrieval) ...

class LocalizationAgent(Agent):
    """
    Concrete agent class for localization tasks.
    """
    def process(self, input_data):
        """
        Localizes the input data.
        """
        print(f"LocalizationAgent processing: {input_data}")
        # ... (Implementation for localization) ...

class TaskAgent(Agent):
    """
    Concrete agent class for performing specific tasks.
    """
    def process(self, input_data):
        """
        Performs a task based on the input.
        """
        print(f"TaskAgent processing: {input_data}")
        # ... (Implementation for task execution) ...

class AgentFactory:
    """
    Factory class for creating different types of agents.
    """
    def create_agent(self, agent_type: str) -> Agent:
        """
        Creates an agent based on the specified type.

        Args:
            agent_type: The type of agent to create (e.g., "retrieval", "localization", "task").

        Returns:
            An instance of the corresponding agent class, or None if the type is invalid.
        """
        if agent_type.lower() == "retrieval":
            return RetrievalAgent()
        elif agent_type.lower() == "localization":
            return LocalizationAgent()
        elif agent_type.lower() == "task":
            return TaskAgent()
        else:
            print(f"Error: Invalid agent type: {agent_type}")
            return None

# Example Usage
if __name__ == "__main__":
    factory = AgentFactory()

    retrieval_agent = factory.create_agent("retrieval")
    if retrieval_agent:
        retrieval_agent.process("search query")

    localization_agent = factory.create_agent("Localization")  # Case-insensitive
    if localization_agent:
        localization_agent.process("text to localize")

    task_agent = factory.create_agent("task")
    if task_agent:
        task_agent.process("task details")

    invalid_agent = factory.create_agent("invalid")  # Handles invalid type