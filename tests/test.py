from src.build_graph import AdjacencyMatrixBuilder, AdjacencyListBuilder
from src.graph_based_cpd import GraphBased

import unittest


# pytest .\tests\test.py


def custom_comparison(node1, node2):
    return abs(node1 - node2) <= 5


class TestGraphCPD(unittest.TestCase):
    def test_graph_matrix(self):
        data_set1 = [50, 55, 60, 48, 52, 70, 75, 80, 90, 85, 95, 100, 50]
        builder = AdjacencyMatrixBuilder(data_set1, custom_comparison)
        mtxgraph = builder.build_graph()

        rg = mtxgraph.check_edges_existence(3)
        self.assertEqual(rg, 5, "Rg(t) is not true")

        num_edges = mtxgraph.num_of_edges
        self.assertEqual(num_edges, 16, "|G| in not true")

        sum_squares_degree = mtxgraph.sum_of_squares_of_degrees_of_nodes()
        self.assertEqual(sum_squares_degree, 96, "Sum of squares of degree  is not true")

    def test_graph_list(self):
        data_set1 = [50, 55, 60, 48, 52, 70, 75, 80, 90, 85, 95, 100, 50]
        builder = AdjacencyListBuilder(data_set1, custom_comparison)
        mtxgraph = builder.build_graph()

        rg = mtxgraph.check_edges_existence(3)
        self.assertEqual(rg, 5, "Rg(t) is not true")

        num_edges = mtxgraph.num_of_edges
        self.assertEqual(num_edges, 16, "|G| in not true")

        sum_squares_degree = mtxgraph.sum_of_squares_of_degrees_of_nodes()
        self.assertEqual(sum_squares_degree, 96, "Sum of squares of degree  is not true")

    def test_CPD_lst(self):
        data_set1 = [50, 55, 60, 48, 52, 70, 75, 80, 90, 85, 95, 100, 50]
        lstbuild = AdjacencyListBuilder(data_set1, custom_comparison)
        lstgraph = lstbuild.build_graph()

        cpdmtx = GraphBased(lstgraph)
        e = cpdmtx.calculation_e(3)
        self.assertEqual(e, 6.153846153846154, msg="E(Rg(t)) is not true")

        var = cpdmtx.calculation_var(3)
        self.assertEqual(var, 6.885422270037656, msg="Var(Rg(t)) is not true")

        z = cpdmtx.calculation_z(3)
        self.assertEqual(z, 0.4397264774834466, msg="Zg(t) is not true")

        z_list = []
        self.assertEqual(cpdmtx.find_changepoint(1.5, z_list), [5], "Incorrect change point")

    def test_CPD_mtx(self):
        data_set1 = [50, 55, 60, 48, 52, 70, 75, 80, 90, 85, 95, 100, 50]
        mtxbuild = AdjacencyMatrixBuilder(data_set1, custom_comparison)
        mtxgraph = mtxbuild.build_graph()

        cpdmtx = GraphBased(mtxgraph)
        e = cpdmtx.calculation_e(3)
        self.assertEqual(e, 6.153846153846154, msg="E(Rg(t)) is not true")

        var = cpdmtx.calculation_var(3)
        self.assertEqual(var, 6.885422270037656, msg="Var(Rg(t)) is not true")

        z = cpdmtx.calculation_z(3)
        self.assertEqual(z, 0.4397264774834466, msg="Zg(t) is not true")

        z_list = []
        self.assertEqual(cpdmtx.find_changepoint(1.5, z_list), [5], "Incorrect change point")
