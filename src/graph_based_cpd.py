import math
from typing import List

from src.build_graph import AdjacencyListBuilder, AdjacencyMatrixBuilder
from src.graph import GraphMatrix, GraphList
from src.interface.CPD import CPD


class GraphBased(CPD):
    def __init__(self, graph):
        super().__init__(graph)
        self.graph = graph

    def calculation_e(self, thao: int) -> float:
        n = len(self.graph.data)
        p1 = ((2 * thao) * (n - thao)) / (n * (n - 1))
        return p1 * self.graph.num_of_edges

    def calculation_var(self, thao: int) -> float:
        n = len(self.graph.data)
        p1 = ((2 * thao) * (n - thao)) / (n * (n - 1))
        p2 = (4 * thao * (thao - 1) * (n - thao) * (n - thao - 1)) / (n * (n - 1) * (n - 2) * (n - 3))
        var = (
            p1 * self.graph.num_of_edges
            + (0.5 * p1 - p2) * self.graph.sum_of_squares_of_degrees_of_nodes()
            + (p2 - p1**2) * self.graph.num_of_edges**2
        )

        return var

    def calculation_z(self, thao: int) -> float:
        zg = -(
            (self.graph.check_edges_existence(thao) - self.calculation_e(thao)) / math.sqrt(self.calculation_var(thao))
        )
        return zg

    def find_changepoint(self, border: float, zlist: List[float]) -> List:
        change_point_list = []
        for t in range(1, len(self.graph.data)):
            zlist.append(self.calculation_z(t))  # Needed for drawing Zg(t) graphics
            if self.calculation_z(t) > border:
                change_point_list.append(t)
        return change_point_list


if __name__ == "__main__":

    def custom_comparison(node1, node2):
        if abs(node1 - node2) <= 5:
            return True
        else:
            return False

    z = []
    data1 = [50, 55, 60, 48, 52, 70, 75, 80, 90, 85, 95, 100]
    builder = AdjacencyMatrixBuilder(data1, custom_comparison)
    mt = builder.build_matrix()
    graph = builder.build_graph()
    print(mt)
    print(graph.check_edges_existence(3))
    print(graph[3][0])
    # a = builder.build_graph()
    # print(a[3][0])
    # gr = GraphMatrix(build)  # or GraphList(build)
    # print(gr.check_edges_existence(3))
