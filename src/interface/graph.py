from abc import ABC, abstractmethod
from typing import List, Any, Callable


class Graph(ABC):
    def __init__(self, data: List[Any], comparing_function: Callable[[Any, Any], bool]):
        self.data = data
        # self.graph_builder = BuilderGraph(data, comparing_function)
        # why doesn't work !?!?
        self.num_of_edges: int = 0

    @abstractmethod
    def check_edges_existence(self, thao: int) -> int:
        pass

    @abstractmethod
    def sum_of_squares_of_degrees_of_nodes(self) -> int:
        pass
