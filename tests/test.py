from src.graph_based_cpd import CPD
from src.net_characteristics import Graph

import unittest


def custom_comparison(node1, node2):
    if abs(node1 - node2) <= 5:
        return True
    else:
        return False


class TestGraphCPD(unittest.TestCase):
    def test_graph1(self):
        data_set1 = [50, 55, 60, 48, 52, 70, 75, 80, 90, 85, 95, 100, 50]
        graph = Graph(data_set1, custom_comparison, "Matrix")
        rg = graph.check_edges_existence(3)
        self.assertEqual(rg, 5, "Rg(t) is not true")

        num_edges = graph.num_of_edges
        self.assertEqual(num_edges, 16, "|G| in not true")

        sum_squares_degree = graph.sum_of_squares_of_degrees_of_nodes()
        self.assertEqual(sum_squares_degree, 96, "Sum of squares of degree  is not true")

    def test_CPD(self):
        data_set1 = [50, 55, 60, 48, 52, 70, 75, 80, 90, 85, 95, 100, 50]
        changepoint = CPD(Graph(data_set1, custom_comparison, "Matrix"))
        e = changepoint.calculation_e(3)
        self.assertEqual(e, 6.153846153846154, "E(Rg(t)) is not true")

        var = changepoint.calculation_var(3)
        self.assertEqual(var, 6.885422270037656, "Var(Rg(t)) is not true")

        z = changepoint.calculation_z(3)
        self.assertEqual(z, 0.4397264774834466, "Zg(t) is not true")
        z_list = []
        self.assertEqual(changepoint.find_changepoint(1.5, z_list), [5], "Incorrect change point")
