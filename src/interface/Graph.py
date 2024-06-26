from abc import ABC, abstractmethod


class IGraph(ABC):
    def __init__(self):
        self.num_of_edges = None
        self.len = None

    @abstractmethod
    def check_edges_existence(self, thao: int) -> int:
        """Calculate R for Adjacency Matrix or List"""
        pass

    @abstractmethod
    def sum_of_squares_of_degrees_of_nodes(self) -> int:
        """Calculate sum of degrees^2 for Adjacency Matrix or List"""
        pass
