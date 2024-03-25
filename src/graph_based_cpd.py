import math
from typing import List

from src.build_graph import AdjacencyListBuilder, AdjacencyMatrixBuilder
from src.interface.CPD import CPD


class GraphBased(CPD):
    def __init__(self, graph):
        super().__init__(graph)
        self.graph = graph
        self.size = graph.len

    def calculation_e(self, thao: int) -> float:
        p1 = ((2 * thao) * (self.size - thao)) / (self.size * (self.size - 1))
        return p1 * self.graph.num_of_edges

    def calculation_var(self, thao: int) -> float:
        p1 = ((2 * thao) * (self.size - thao)) / (self.size * (self.size - 1))
        p2 = (4 * thao * (thao - 1) * (self.size - thao) * (self.size - thao - 1)) / (
            self.size * (self.size - 1) * (self.size - 2) * (self.size - 3)
        )
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
        for t in range(1, self.size):
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
    data1 = [50, 55, 60, 48, 52, 70, 75, 80, 90, 85, 95, 100, 50]
    builder = AdjacencyMatrixBuilder(data1, custom_comparison)
    mtxgraph = builder.build_graph()

    lstbuild = AdjacencyListBuilder(data1, custom_comparison)
    lstgraph = lstbuild.build_graph()

    cpdmtx = GraphBased(mtxgraph)
    cpdlst = GraphBased(lstgraph)
    print(cpdmtx.calculation_z(3))
    print(cpdlst.calculation_z(3))
