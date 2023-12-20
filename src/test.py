from main import Graph, CPD
import unittest


class TestGraphCPD(unittest.TestCase):
    def custom_comparison(self, node1, node2):
        if abs(node1 - node2) <= 5:
            return True
        else:
            return False

    def test_graph1(self):
        data_set1 = [50, 55, 60, 48, 52, 70, 75, 80, 90, 85, 95, 100, 50]
        graph = Graph(data_set1, self.custom_comparison)
        rg = graph.check_edges_existence(3)
        self.assertEqual(rg, 5, "Rg(t) is not true")

        num_edges = graph.calculateEdges()
        self.assertEqual(num_edges, 16, "|G| in not true")

        sum_squares_degree = graph.sumOfSquaresOfDegreesOfNodes()
        self.assertEqual(sum_squares_degree, 96, "Sum of squares of degree  is not true")

    def test_CPD(self):
        data_set1 = [50, 55, 60, 48, 52, 70, 75, 80, 90, 85, 95, 100, 50]
        changepoint = CPD(Graph(data_set1, self.custom_comparison))
        e = changepoint.calculation_E(3)
        self.assertEqual(e, 6.153846153846154, "E(Rg(t)) is not true")

        var = changepoint.calculation_Var(3)
        self.assertEqual(var, 2.7455621301775164, "Var(Rg(t)) is not true")

        z = changepoint.calculation_z(3)
        self.assertEqual(z, 0.6963575181639445, "Zg(t) is not true")
        z_list = []
        self.assertEqual(changepoint.find_changepoint(2, z_list), [5], "Incorrect change point")
