import math

import numpy as np


class GraphBuilder:
    def __init__(self, data, user_function):
        self.data = data
        self.user_function = user_function
        self.graph_build = self.AdjacencyMatrix()

    def AdjacencyMatrix(self):
        count_nodes = len(self.data)
        adjacency_matrix = np.zeros((count_nodes, count_nodes), dtype=int)

        for i in range(count_nodes):
            for j in range(count_nodes):
                if self.user_function(self.data[i], self.data[j]) and (i != j):
                    adjacency_matrix[i, j] = 1

        return adjacency_matrix

    def AdjacencyList(self):
        count_nodes = len(self.data)
        adjacency_list = {index: [] for index in range(count_nodes)}

        for i in range(count_nodes):
            for j in range(count_nodes):
                if self.user_function(self.data[i], self.data[j]) and (i != j):
                    if self.data[j] not in adjacency_list[i]:
                        adjacency_list[i].append(j)

        for node, neighbors in adjacency_list.items():
            print(f"{self.data[node]}: {[self.data[index] for index in neighbors]}")

        return adjacency_list


class Graph:
    def __init__(self, data, user_function):
        self.data = data
        self.graph_builder = GraphBuilder(self.data, user_function)

    def calculateEdges(self):
        count = 0
        for node_1 in range(len(self.data)):
            for node_2 in range(len(self.data)):
                if self.graph_builder.graph_build[node_1, node_2] != 0 and (node_1 != node_2):
                    count += 1
        return count / 2

    def calculateEdges_list(self):
        unique_edges = set()

        for node, neighbors in self.graph_builder.graph_build.items():
            for neighbor_index in neighbors:
                edge = tuple(sorted((node, neighbor_index)))
                unique_edges.add(edge)

        return len(unique_edges)

    def check_edges_existence(self, thao):
        count_edges = 0
        for nodeBefore in range(thao):
            for nodeAfter in range(thao, len(self.data)):
                if self.graph_builder.graph_build[nodeBefore, nodeAfter] == 1:
                    count_edges += 1
        return count_edges

    def check_edges_existence_list(self, thao):
        count_edges = 0
        for node_1 in range(thao):
            for node_2 in range(thao, len(self.data)):
                if self.data[node_2] in self.graph_builder.graph_build[self.data[node_1]]:
                    count_edges += 1

        return count_edges

    def sumOfSquaresOfDegreesOfNodes(self):
        sum_squares = 0
        for node_1 in range(len(self.data)):
            node_degree = 0
            for node_2 in range(len(self.data)):
                if self.graph_builder.graph_build[node_1, node_2] == 1:
                    node_degree += 1
            node_degree = node_degree**2
            sum_squares += node_degree
        return sum_squares

    def sumOfSquaresOfDegreesOfNodes_List(self):
        sum_squares = 0
        for node in range(len(self.data)):
            sum_squares += len(self.graph_builder.graph_build[node]) ** 2
        return sum_squares


class CPD:
    def __init__(self, graph):
        self.graph = graph

    def calculation_E(self, thao):
        n = len(self.graph.data)
        p1 = ((2 * thao) * (n - thao)) / (n * (n - 1))
        return p1 * self.graph.calculateEdges()

    def calculation_Var(self, thao):
        n = len(self.graph.data)
        p1 = ((2 * thao) * (n - thao)) / (n * (n - 1))
        p2 = (4 * thao * (thao - 1) * (n - thao) * (n - thao - 1)) / (n * (n - 1) * (n - 2) * (n - 3))
        var = (
            p1 * self.graph.calculateEdges()
            + (0.5 * p1 - p2) * self.graph.sumOfSquaresOfDegreesOfNodes()
            + (p2 - p1**2) * self.graph.calculateEdges() ** 2
        )

        return var

    def calculation_z(self, thao):
        zg = -(
            (self.graph.check_edges_existence(thao) - self.calculation_E(thao)) / math.sqrt(self.calculation_Var(thao))
        )
        return zg

    def find_changepoint(self, border, zlist):
        change_point_list = []
        for t in range(1, len(self.graph.data)):
            zlist.append(self.calculation_z(t))  # Needed for drawing Zg(t) graphics
            if self.calculation_z(t) > border:
                change_point_list.append(t)
        return change_point_list


if __name__ == "__main__":

    def custom_comparison(node1, node2):
        if abs(node1 - node2) <= 1:
            return True
        else:
            return False

    normal_data = np.random.normal(loc=0, scale=1, size=50)
    normal_z = []
    normal_graph = Graph(normal_data, custom_comparison)
    normal_CPD = CPD(normal_graph)
    for i in range(1, len(normal_data)):
        normal_z.append(normal_CPD.calculation_z(i))
    print(normal_z)
