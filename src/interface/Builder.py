from abc import ABC, abstractmethod
from typing import List, Any, Callable, Dict

import numpy as np

from src.interface.Graph import IGraph, IGraphList, IGraphMatrix


class IBuilderGraph(ABC):
    def __init__(self, data: List[Any], comparing_function: Callable[[Any, Any], bool], type_graph: str = "List"):
        self.data = data
        self.comparing_function = comparing_function
        self.type = type_graph
        self.num_of_edges: int = 0

    @abstractmethod
    def build_graph(self) -> IGraph:
        if self.type == "List":
            graph = IAdjacencyListBuilder(self.data, self.comparing_function)
            return IGraphList(graph)
        elif self.type == "Matrix":
            graph: np.array = IAdjacencyMatrixBuilder(self.data, self.comparing_function)
            return IGraphMatrix(graph)
        """ Build and return a graph Adjacency List or Adjacency Matrix """
        pass


class IAdjacencyListBuilder(IBuilderGraph):
    def __init__(self, data: List[Any], comparing_function: Callable[[Any, Any], bool]):
        super().__init__(data, comparing_function)
        self.data = data
        self.comparing_function = comparing_function
        self.num_of_edges: int = 0

    def build_graph(self) -> IGraphList:
        graph: Dict[int, List[int]] = {}  # Placeholder, replace with actual implementation
        return IGraphList(graph)


class IAdjacencyMatrixBuilder(IBuilderGraph):
    def __init__(self, data: List[Any], comparing_function: Callable[[Any, Any], bool]):
        super().__init__(data, comparing_function)
        self.data = data
        self.comparing_function = comparing_function
        self.num_of_edges: int = 0

    def build_graph(self) -> IGraphMatrix:
        """Build and return a graph Adjacency Matrix"""
        graph: np.ndarray = np.zeros((self.data[0], self.data[1]))
        return IGraphMatrix(graph)
