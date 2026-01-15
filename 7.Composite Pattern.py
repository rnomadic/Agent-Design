from abc import ABC, abstractmethod

# Component Interface
class AgentComponent(ABC):
    @abstractmethod
    def execute(self):
        pass

# Leaf Agent
class AIWorker(AgentComponent):
    def __init__(self, name):
        self.name = name
    
    def execute(self):
        print(f"{self.name} is executing its task.")

# Composite Agent (Can contain multiple agents)
class AICompositeAgent(AgentComponent):
    def __init__(self, name):
        self.name = name
        self.sub_agents = []
    
    def add_agent(self, agent):
        self.sub_agents.append(agent)
    
    def remove_agent(self, agent):
        self.sub_agents.remove(agent)
    
    def execute(self):
        print(f"{self.name} is delegating tasks to sub-agents...")
        for agent in self.sub_agents:
            agent.execute()

# Demonstration
worker1 = AIWorker("Worker 1")
worker2 = AIWorker("Worker 2")
worker3 = AIWorker("Worker 3")

team_lead = AICompositeAgent("Team Lead")
team_lead.add_agent(worker1)
team_lead.add_agent(worker2)

manager = AICompositeAgent("Manager")
manager.add_agent(team_lead)
manager.add_agent(worker3)

print("Executing tasks in hierarchy:")
manager.execute()