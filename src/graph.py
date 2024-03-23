from typing import Any

from numpy import ndarray, dtype

from src.interface.Graph import IGraph


class GraphMatrix(IGraph):
    def __init__(self, mtx: ndarray[Any, dtype], size: int, num_of_edges: int):
        self.mtx = mtx
        self.len = size
        self.num_of_edges: int = num_of_edges

    def __getitem__(self, item):
        return self.mtx[item]

    def check_edges_existence(self, thao: int) -> int:
        count_edges = 0
        for node_before in range(thao):
            for node_after in range(thao, self.len):
                if self.mtx[node_before, node_after] == 1:
                    count_edges += 1
        return count_edges

    def sum_of_squares_of_degrees_of_nodes(self) -> int:
        sum_squares = 0
        for node_1 in range(0, self.len):
            node_degree = 0
            for node_2 in range(0, self.len):
                if self.mtx[node_1, node_2] == 1:
                    node_degree += 1
            node_degree = node_degree**2
            sum_squares += node_degree
        return sum_squares


class GraphList(IGraph):
    def __init__(self, lst, data, num_of_edges: int):
        self.lst = lst
        self.data = data
        self.num_of_edges: int = num_of_edges

    def __getitem__(self, item):
        return self.lst[item]

    def check_edges_existence(self, thao) -> int:
        count_edges = 0
        for node_1 in range(thao):
            for node_2 in range(0, len(self.data)):
                if self.data[node_2] in self.lst[node_1]:
                    count_edges += 1
        return count_edges // 2

    def sum_of_squares_of_degrees_of_nodes(self) -> int:
        sum_squares = 0
        for node in range(0, len(self.data)):
            sum_squares += len(self.lst[node]) ** 2
        return sum_squares
