import json
from typing import Callable, Any

from src.build_graph import AdjacencyMatrixBuilder
from src.graph_based_cpd import GraphBased
from src.interface.Builder import IBuilderGraph
from src.interface.Graph import IGraph


def read_single_element(filename: str):
    with open(filename, "r") as fr:
        data = json.load(fr)
    for element in data:
        yield element


def online(comparing_fnc: Callable[[Any, Any], bool], border: Any, detect: int = 25):  # 25 оптимально с border 4.3
    bld: IBuilderGraph
    grph: IGraph
    cpd: GraphBased
    data = []
    data_generator = read_single_element("file.txt")

    print("Введите данные (или 'exit' для завершения): ")
    while True:
        # Принимаем данные от пользователя или из другого источника
        # user_input = input()
        try:
            user_input = next(data_generator)
        except StopIteration:
            break
        # if user_input.lower() == 'exit':  # TODO: Почище сделать (Красивее)
        if user_input == "exit":
            current_data = data[-detect:]
            print(current_data)
            bld = AdjacencyMatrixBuilder(current_data, comparing_fnc)
            grph = bld.build_graph()
            cpd = GraphBased(grph)
            print(data)
            print(f"Change Point: {cpd.find_changepoint(border, [])}")
            print("Завершение работы программы.")
            break

        # data.extend([int(item.strip(',')) for item in user_input.split()])
        # cnt += len(user_input.split())
        data.append(user_input)

        if len(data) == detect:
            bld = AdjacencyMatrixBuilder(data, comparing_fnc)
            grph = bld.build_graph()
            cpd = GraphBased(grph)
            # print(data)
            print(f"Change Point: {cpd.find_changepoint(border, [])}")

        # if grph is not None:

        if len(data) % detect - 10 == 0 and len(data) > detect:
            current_data = data[-detect:]
            # print(current_data)
            bld = AdjacencyMatrixBuilder(current_data, comparing_fnc)  # TODO: add and delete data in a graph
            grph = bld.build_graph()
            cpd = GraphBased(grph)
            # print(data)
            print(f"Change Point: {cpd.find_changepoint(border, [])}")
            # print(cpd.calculation_z(3))

        # print(data)


def custom_comparison(node1, node2):
    return abs(node1 - node2) <= 5


online(custom_comparison, 4.3)

# 70, 75, 80, 90, 85, 95, 100, 78, 83, 94, 45, 42, 40, 38, 35, 30, 28, 25, 20, 18, 15, 12, 10, 8, 5
# 9, 10, 4, 14, 14, 15, 8, 20, 23, 19, 114, 110, 119, 120, 115, 118, 110, 109, 105, 100, 113, 110, 119, 125, 107
