# Graph-Based Change-point-detection


# How to use
To create a graph, you need to pass some `data` and `threshold` 

```python
analyzer = GraphCPD(data, threshold)
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


# License
Distributed under the MIT License. See [LICENSE](https://github.com/Lesh79/Change-point-detection/blob/main/LICENSE) for more information.

