from abc import ABC

from src.interface.Graph import IGraph, IGraphMatrix, IGraphList


class Graph(IGraph):
    def __init__(self, graph, type_graph: str = "List"):
        super().__init__(graph, type_graph)
        self.graph = graph
        self.type = type_graph
        self.num_of_edges: int = graph.num_of_edges

    def check_edges_existence(self, thao: int) -> int:
        if self.type == "List":
            return GraphList(self.graph).check_edges_existence(thao)
        elif self.type == "Matrix":
            return GraphMatrix(self.graph).check_edges_existence(thao)

    def sum_of_squares_of_degrees_of_nodes(self) -> int:
        if self.type == "List":
            return GraphList(self.graph).sum_of_squares_of_degrees_of_nodes()
        elif self.type == "Matrix":
            return GraphMatrix(self.graph).sum_of_squares_of_degrees_of_nodes_matrix()


class GraphMatrix(IGraphMatrix, ABC):
    def __init__(self, graph):
        super().__init__(graph)
        self.graph = graph
        self.data = graph.data
        self.num_of_edges: int = graph.num_of_edges

    def check_edges_existence_matrix(self, thao: int) -> int:
        count_edges = 0
        for node_before in range(thao):
            for node_after in range(thao, len(self.data)):
                if self.graph.build_graph()[node_before, node_after] == 1:
                    count_edges += 1
        return count_edges

    def sum_of_squares_of_degrees_of_nodes_matrix(self) -> int:
        sum_squares = 0
        for node_1 in range(len(self.data)):
            node_degree = 0
            for node_2 in range(len(self.data)):
                if self.graph.build_graph()[node_1, node_2] == 1:
                    node_degree += 1
            node_degree = node_degree**2
            sum_squares += node_degree
        return sum_squares


class GraphList(IGraphList, ABC):
    def __init__(self, graph):
        super().__init__(graph)
        self.graph = graph
        self.data = graph.data
        self.num_of_edges: int = graph.num_of_edges

    def check_edges_existence(self, thao) -> int:
        count_edges = 0
        for node_1 in range(thao):
            for node_2 in range(thao, len(self.data)):
                if node_2 in self.graph.build_graph()[node_1]:
                    count_edges += 1
        return count_edges

    def sum_of_squares_of_degrees_of_nodes(self) -> int:
        sum_squares = 0
        for node in range(len(self.data)):
            sum_squares += len(self.graph.build_graph()[node]) ** 2
        return sum_squares
