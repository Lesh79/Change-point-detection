from typing import List, Any, Callable

import numpy as np

from src.graph import GraphList, GraphMatrix
from src.interface.Builder import IBuilderGraph, IAdjacencyMatrixBuilder, IAdjacencyListBuilder
from src.interface.Graph import IGraph


class BuildGraph(IBuilderGraph):
    def __init__(self, data: List[List[Any]], comparing_function: Callable[[Any, Any], bool], type_graph: str = "List"):
        super().__init__(data, comparing_function, type_graph)
        self.data = data
        self.comparing_function = comparing_function
        self.type = type_graph
        self.num_of_edges: int = 0

    def build_graph(self) -> IGraph:
        if self.type == "List":
            graph = AdjacencyListBuilder(self.data, self.comparing_function)
            self.num_of_edges = graph.num_of_edges
            return GraphList(graph)
        if self.type == "Matrix":
            graph = AdjacencyMatrixBuilder(self.data, self.comparing_function)
            self.num_of_edges = graph.num_of_edges
            return GraphMatrix(graph)

    def __call__(self):
        self.build_graph()


class AdjacencyMatrixBuilder(IAdjacencyMatrixBuilder):
    def __init__(self, data: List[Any], comparing_function: Callable[[Any, Any], bool]):
        super().__init__(data, comparing_function)
        self.data = data
        self.comparing_function = comparing_function
        self.num_of_edges: int = 0

    # def __call__(self):
    #     self.build_graph()

    def build_graph(self) -> GraphMatrix:  # Adjacency Matrix
        count_edges = 0
        count_nodes = len(self.data)
        adjacency_matrix = np.zeros((count_nodes, count_nodes), dtype=int)

        for i in range(count_nodes):
            for j in range(count_nodes):
                if self.comparing_function(self.data[i], self.data[j]) and (i != j):
                    adjacency_matrix[i, j] = 1
                    count_edges += 1
        self.num_of_edges = count_edges // 2

        return GraphMatrix(adjacency_matrix)


class AdjacencyListBuilder(IAdjacencyListBuilder):
    def __init__(self, data: List[Any], comparing_function: Callable[[Any, Any], bool]):
        super().__init__(data, comparing_function)
        self.data = data
        self.comparing_function = comparing_function
        self.num_of_edges: int = 0

    # def __call__(self):
    #     self.build_graph()

    def build_graph(self) -> GraphList:  # Adjacency List
        unique_edges = set()
        count_nodes = len(self.data)
        adjacency_list = {index: [] for index in range(count_nodes)}

        for i in range(count_nodes):
            for j in range(count_nodes):
                if self.comparing_function(self.data[i], self.data[j]) and (i != j):
                    if self.data[j] not in adjacency_list[i]:
                        adjacency_list[i].append(j)
                        edge = tuple(sorted((i, j)))
                        unique_edges.add(edge)
        self.num_of_edges = len(unique_edges)

        # for node, neighbors in adjacency_list.items():
        #     print(f"{self.data[node]}: {[self.data[index] for index in neighbors]}")

        return GraphList(adjacency_list)
