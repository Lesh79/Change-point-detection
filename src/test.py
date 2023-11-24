from main import *
import unittest


class test_GraphCPD(unittest.TestCase):

    def test_graph1(self):
        data_set1 = [50, 55, 60, 48, 52, 70, 75, 80, 90, 85, 95, 100, 50]
        graph1 = GraphCPD(data_set1,5)
        Rg = graph1.check_edges_existence(3)
        self.assertEqual(Rg, 5, "Rg(t) is not true")

        numOfEdges = graph1.calculateEdges()
        self.assertEqual(numOfEdges, 16, "|G| in not true")

        sum_squares_degree = graph1.sumOfSquaresOfDegreesOfNodes()
        self.assertEqual(sum_squares_degree, 96, "Sum of squares of degree  is not true")

        e = graph1.calculation_E(3)
        self.assertEqual(e, 6.153846153846154, "E(Rg(t)) is not true")

        var = graph1.calculation_Var(3)
        self.assertEqual(var, 2.7455621301775164, "Var(Rg(t)) is not true")

        z = graph1.calculation_z(3)
        self.assertEqual(z, 0.6963575181639445, "Zg(t) is not true")

        self.assertEqual(graph1.find_changepoint(1), 5, "Incorrect change point")

    # def test_graph2(self):
    #     data_set1 = [20, 22, 25, 24, 23, 26, 28, 32, 35, 36, 38, 37, 35,34, 33,  ]
    #     graph1 = GraphCPD(data_set1,2,11)
    #     Rg = graph1.check_edges_existence()
    #     self.assertEqual(Rg, 10, "Rg(t) is not true")
    #
    #     numOfEdges = graph1.calculateEdges()
    #     self.assertEqual(numOfEdges, 25, "|G| in not true")
    #
    #     sum_squares_degree = graph1.sumOfSquaresOfDegreesOfNodes()
    #     self.assertEqual(sum_squares_degree, 194, "Sum of squares of degree  is not true")
    #
    #     e = graph1.calculation_E()
    #     self.assertEqual(e, 10.476190476190476, "E(Rg(t)) is not true")
    #
    #     var = graph1.calculation_Var()
    #     self.assertEqual(var, 4.3915576487005, "Var(Rg(t)) is not true")
    #
    #     z = graph1.calculation_z()
    #     self.assertEqual(z, 0.22723300469490545, "Zg(t) is not true")
    #
    #     self.assertEqual(graph1.find_changepoint(0.1), "Change point", "IDI NAHUI NICHEGO NE IZMENILOS")
