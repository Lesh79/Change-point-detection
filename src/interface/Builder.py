from abc import ABC, abstractmethod
from typing import List, Any, Callable


from src.interface.Graph import IGraph


class IBuilderGraph(ABC):
    def __init__(self, data: List[Any], comparing_function: Callable[[Any, Any], bool]):
        self.data = data
        self.comparing_function = comparing_function
        self.num_of_edges: int = 0

    @abstractmethod
    def build_graph(self) -> IGraph:
        """Build and return a graph Adjacency List or Adjacency Matrix"""
        pass
