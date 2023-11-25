import math

import pandas as pd


class GraphCPD:
    def __init__(self, data, user_function):
        self.data = data
        self.user_function = user_function
        self.graph = self.AdjacencyMatrix()

    def AdjacencyMatrix(self):
        count_nodes = len(self.data)

        adjacency_matrix = pd.DataFrame(index=self.data, columns=self.data)

        for i in range(count_nodes):
            for j in range(count_nodes):
                if self.user_function(self.data[i], self.data[j]) and (i != j):
                    adjacency_matrix.iloc[i, j] = 1

        return adjacency_matrix

    def AdjacencyList(self):
        count_nodes = len(self.data)
        adjacency_list = {index: [] for index in range(count_nodes)}

        for i in range(count_nodes):
            for j in range(count_nodes):
                if self.user_function(self.data[i], self.data[j]) and (i != j):
                    if self.data[j] not in adjacency_list[i]:
                        adjacency_list[i].append(j)

        # for node, neighbors in adjacency_list.items():
        #     print(f"{self.data[node]}: {[self.data[index] for index in neighbors]}")

        return adjacency_list

    def check_edges_existence(self, thao):
        count_edges = 0
        for nodeBefore in range(thao):
            for nodeAfter in range(thao, len(self.data)):
                if not pd.isna(self.graph.iloc[nodeBefore, nodeAfter]):
                    count_edges += 1
        return count_edges

    def check_edges_existence_list(self, thao):
        count_edges = 0
        for node_1 in range(thao):
            for node_2 in range(thao, len(self.data)):
                if self.data[node_2] in self.AdjacencyList()[self.data[node_1]]:
                    count_edges += 1

        return count_edges

    def calculateEdges(self):
        count = 0
        for node_1 in range(len(self.data)):
            for node_2 in range(len(self.data)):
                if not pd.isna(self.graph.iloc[node_1, node_2]):
                    count += 1
        return count / 2

    def calculateEdges2(self):
        unique_edges = set()

        for node, neighbors in self.AdjacencyList().items():
            for neighbor_index in neighbors:
                edge = tuple(sorted((node, neighbor_index)))
                unique_edges.add(edge)

        return len(unique_edges)

    def sumOfSquaresOfDegreesOfNodes(self):
        sum_squares = 0
        for node_1 in range(len(self.data)):
            node_degree = 0
            for node_2 in range(len(self.data)):
                if not pd.isna((self.graph.iloc[node_1, node_2])):
                    node_degree += 1
            node_degree = node_degree**2
            sum_squares += node_degree
        return sum_squares

    def sumOfSquaresOfDegreesOfNodes_List(self):
        sum_squares = 0
        for node in range(len(self.data)):
            sum_squares += len(self.AdjacencyList()[node]) ** 2
        return sum_squares

    def calculation_E(self, thao):
        n = len(self.data)
        p1 = ((2 * thao) * (n - thao)) / (n * (n - 1))
        return p1 * self.calculateEdges()

    def calculation_Var(self, thao):
        n = len(self.data)
        p1 = ((2 * thao) * (n - thao)) / (n * (n - 1))
        p2 = (4 * thao * (thao - 1) * (n - thao) * (n - thao - 1)) / (n * (n - 1) * (n - 2) * (n - 3))
        var = (
            p2 * self.calculateEdges()
            + (0.5 * p1 - p2) * self.sumOfSquaresOfDegreesOfNodes()
            + (p2 - p1**2) * self.calculateEdges() ** 2
        )

        return var

    def calculation_z(self, thao):
        zg = -((self.check_edges_existence(thao) - self.calculation_E(thao)) / math.sqrt(self.calculation_Var(thao)))
        return zg

    def find_changepoint(self, border):
        self.AdjacencyMatrix()
        for t in range(1, len(self.data)):
            if self.calculation_z(t) > border:
                return t


if __name__ == "__main__":

    def custom_comparison(node1, node2):
        if abs(node1 - node2) <= 5:
            return True
        else:
            return False

    data_1 = [50, 55, 60, 48, 52, 70, 75, 80, 90, 85, 95, 100, 50]
    data_2 = [
        20,
        22,
        25,
        24,
        23,
        26,
        28,
        32,
        35,
        36,
        38,
        37,
        35,
        34,
        33,
    ]
    analyzer = GraphCPD(data_1, custom_comparison)
