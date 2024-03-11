from typing import List
import math
from src.net_characteristics import Graph


class CPD:
    def __init__(self, graph: Graph):
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
        if abs(node1 - node2) <= 10:
            return True
        else:
            return False

    z = []
    data1 = [50, 55, 60, 48, 52, 70, 75, 80, 90, 85, 95, 100]
    graph1 = Graph(data1, custom_comparison, "Matrix")
    print(graph1.num_of_edges)
    # print(graph.calculate_edges_list())
    # print(graph.check_edges_existence_list(2))
    # print(graph.sum_of_squares_of_degrees_of_nodes_list())
    normal_cpd = CPD(graph1)
    print(normal_cpd.find_changepoint(1, z))
