from abc import ABC, abstractmethod
from typing import List, Any, Dict, Callable


class BuilderGraph(ABC):
    def __init__(self, data: List[Any], comparing_function: Callable[[Any, Any], bool]):
        self.data = data
        self.comparing_function = comparing_function
        self.number_of_edges: int = 0
        self.graph = self.build_graph

    @abstractmethod
    def build_graph(self):
        """ "Build a graph Adjacency List or Adjacency Matrix"""
        pass
