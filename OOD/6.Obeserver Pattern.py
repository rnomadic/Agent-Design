
"""
In this implementation agents (observers) subscribe to updates from a leader agent (observable). 
When the leader agent changes its state, all subscribed agents receive the update.
"""
from abc import ABC, abstractmethod

#Subject observable
class AgentObservable(ABC):
    def __init__(self):
        self._observers = [] #Protected varible

    def add_observers(self, observer):
        self._observers.append(observer)

    def remove_observers(self, observer):
        self.observers.remove(observer)

    def notify_observers(self, message):
        for observer in self._observers:
            observer.update(message)
    

#Observer Interface
class AgentObserver(ABC):
    @abstractmethod
    def update(self, message):
        pass

#Concrete observable agent (base methods + additional features)
class AILeaderAgent(AgentObservable):
    def set_state(self, state):
        print(f"AILeaderAgent: Changing state to {state}")
        self.notify_observers(state)

#Concrete observer agent
class AISubscriberAgent(AgentObserver):
    def __init__(self, name):
        self.name = name
    
    def update(self, message):
        print(f"{self.name} received update: {message}")

#Demonstration
leader = AILeaderAgent()
worker1 = AISubscriberAgent("worker1")
worker2 = AISubscriberAgent("worker2")

leader.add_observers(worker1)
leader.add_observers(worker2)

leader.set_state("task assigned")
leader.set_state("task complete")
