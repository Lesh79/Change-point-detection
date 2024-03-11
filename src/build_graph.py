from typing import List, Any, Dict
import numpy as np
from src.interface.builder_graph import BuilderGraph


class AdjacencyMatrixBuilder(BuilderGraph):
    def __init__(self, data: List[Any], comparing_function):
        super().__init__(data, comparing_function)
        self.data = data
        self.comparing_function = comparing_function
        self.num_of_edges: int = 0
        self.graph = self.build_graph()

    def build_graph(self) -> np.ndarray:  # Adjacency Matrix
        count_edges = 0
        count_nodes = len(self.data)
        adjacency_matrix = np.zeros((count_nodes, count_nodes), dtype=int)

        for i in range(count_nodes):
            for j in range(count_nodes):
                if self.comparing_function(self.data[i], self.data[j]) and (i != j):
                    adjacency_matrix[i, j] = 1
                    count_edges += 1
        self.num_of_edges = count_edges // 2

        return adjacency_matrix


class AdjacencyListBuilder:
    def __init__(self, data: List[Any], comparing_function):
        self.data = data
        self.comparing_function = comparing_function
        self.num_of_edges: int = 0
        self.graph = self.build_graph()

    def build_graph(self) -> Dict[int, List[int]]:  # Adjacency List
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

        return adjacency_list
