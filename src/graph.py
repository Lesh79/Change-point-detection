from typing import List, Any
from src.build_graph import AdjacencyMatrixBuilder, AdjacencyListBuilder
from src.interface.graph import Graph


class GraphMatrix(Graph):
    def __init__(self, data: List[Any], comparing_function):
        super().__init__(data, comparing_function)
        self.data = data
        self.graph_builder = AdjacencyMatrixBuilder(data, comparing_function)
        self.num_of_edges = self.graph_builder.num_of_edges

    def check_edges_existence(self, thao: int) -> int:
        count_edges = 0
        for node_before in range(thao):
            for node_after in range(thao, len(self.data)):
                if self.graph_builder.build_graph()[node_before, node_after] == 1:
                    count_edges += 1
        return count_edges

    def sum_of_squares_of_degrees_of_nodes(self) -> int:
        sum_squares = 0
        for node_1 in range(len(self.data)):
            node_degree = 0
            for node_2 in range(len(self.data)):
                if self.graph_builder.build_graph()[node_1, node_2] == 1:
                    node_degree += 1
            node_degree = node_degree**2
            sum_squares += node_degree
        return sum_squares


class GraphList(Graph):
    def __init__(self, data: List[Any], comparing_function):
        super().__init__(data, comparing_function)
        self.data = data
        self.graph_builder = AdjacencyListBuilder(data, comparing_function)
        self.num_of_edges = self.graph_builder.num_of_edges

    def check_edges_existence(self, thao) -> int:
        count_edges = 0
        for node_1 in range(thao):
            for node_2 in range(thao, len(self.data)):
                if node_2 in self.graph_builder.build_graph()[node_1]:
                    count_edges += 1
        return count_edges

    def sum_of_squares_of_degrees_of_nodes(self) -> int:
        sum_squares = 0
        for node in range(len(self.data)):
            sum_squares += len(self.graph_builder.build_graph()[node]) ** 2
        return sum_squares
