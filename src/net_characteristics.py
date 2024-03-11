from typing import List, Any
from src.build_graph import AdjacencyMatrixBuilder, AdjacencyListBuilder


class Graph:
    def __init__(self, data: List[Any], comparing_function, type_of_graph: str):
        self.data = data
        if type_of_graph == "Matrix":
            self.graph_builder = AdjacencyMatrixBuilder(data, comparing_function)
        elif type_of_graph == "List":
            self.graph_builder = AdjacencyListBuilder(data, comparing_function)
        else:
            raise TypeError("Error in choosing the graph type")
        self.num_of_edges = self.graph_builder.num_of_edges

    def check_edges_existence(self, thao: int) -> int:
        if isinstance(self.graph_builder, AdjacencyMatrixBuilder):
            count_edges = 0
            for node_before in range(thao):
                for node_after in range(thao, len(self.data)):
                    if self.graph_builder.build_adjacency_matrix()[node_before, node_after] == 1:
                        count_edges += 1
            return count_edges
        else:
            raise AttributeError("Error in selecting a function for the graph type")

    def check_edges_existence_list(self, thao) -> int:
        if isinstance(self.graph_builder, AdjacencyListBuilder):
            count_edges = 0
            for node_1 in range(thao):
                for node_2 in range(thao, len(self.data)):
                    if node_2 in self.graph_builder.build_adjacency_list()[node_1]:
                        count_edges += 1
            return count_edges
        else:
            raise AttributeError("Error in selecting a function for the graph type")

    def sum_of_squares_of_degrees_of_nodes(self) -> int:
        if isinstance(self.graph_builder, AdjacencyMatrixBuilder):
            sum_squares = 0
            for node_1 in range(len(self.data)):
                node_degree = 0
                for node_2 in range(len(self.data)):
                    if self.graph_builder.build_adjacency_matrix()[node_1, node_2] == 1:
                        node_degree += 1
                node_degree = node_degree**2
                sum_squares += node_degree
            return sum_squares
        else:
            raise AttributeError("Error in selecting a function for the graph")

    def sum_of_squares_of_degrees_of_nodes_list(self) -> int:
        if isinstance(self.graph_builder, AdjacencyListBuilder):
            sum_squares = 0
            for node in range(len(self.data)):
                sum_squares += len(self.graph_builder.build_adjacency_list()[node]) ** 2
            return sum_squares
        else:
            raise AttributeError("Error in selecting a function for the")
