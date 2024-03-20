from abc import ABC, abstractmethod

import numpy as np


class IGraph(ABC):
    def __init__(self, graph, type_graph: str = "List"):
        self.graph = graph
        self.type = type_graph
        self.num_of_edges: int = 0

    @abstractmethod
    def check_edges_existence(self, thao: int) -> int:
        if self.type == "List":
            return IGraphList(self.graph).check_edges_existence(thao)
        elif self.type == "Matrix":
            return IGraphMatrix(self.graph).check_edges_existence(thao)
        """Calculate R for Adjacency Matrix or List"""

    @abstractmethod
    def sum_of_squares_of_degrees_of_nodes(self) -> int:
        if self.type == "List":
            return IGraphList(self.graph).sum_of_squares_of_degrees_of_nodes()
        elif self.type == "Matrix":
            return IGraphMatrix(self.graph).sum_of_squares_of_degrees_of_nodes()
        """Calculate sum of degrees^2 for Adjacency Matrix or List"""


class IGraphList(IGraph):
    def __init__(self, graph):
        super().__init__(graph)
        self.graph = graph
        self.num_of_edges: int = 0

    @abstractmethod
    def check_edges_existence(self, thao: int) -> int:
        """Calculate R for Adjacency List"""
        pass

    @abstractmethod
    def sum_of_squares_of_degrees_of_nodes(self) -> int:
        """Calculate sum of degrees^2 for Adjacency List"""
        pass


class IGraphMatrix(IGraph):
    def __init__(self, graph):
        super().__init__(graph)
        self.graph = np.ndarray
        self.num_of_edges: int = 0

    @abstractmethod
    def check_edges_existence(self, thao: int) -> int:
        """Calculate R for Adjacency Matrix"""
        pass

    @abstractmethod
    def sum_of_squares_of_degrees_of_nodes(self) -> int:
        """Calculate sum of degrees^2 for Adjacency Matrix"""
        pass
