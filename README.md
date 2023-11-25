# Graph-Based Change-point-detection


# How to use
To create a graph, you need to pass some `data` and `user_function`
```python
analyzer = GraphCPD(data, user_function)
```
`user_function` This is your function that you pass in to compare your data
```python
def custom_comparison(node1, node2):
    if abs(node1 - node2) <= 5:
        return True
    else:
        return False
```

To find change point, you need to call the function `.find_changepoint(border)` and pass `border`
```python
change_point = analyzer.find_changepoint(border)
```
You can calculate quantity of edges in graph
```python
.calculateEdges()
```
You can check how many nodes from first part are connected with nodes from second part
```python
.check_edges_existence(time)
```
# Pre-commit
```bash
pip install pre-commit
```
```bash
pre-commit install
```
# License
Distributed under the MIT License. See [LICENSE](https://github.com/Lesh79/Change-point-detection/blob/main/LICENSE) for more information.
