def ReadGraph(strArr):
    count = int(strArr[0])
    graph = {}
    for node in strArr[1:(count+1)]:
        graph[node] = {}
    for edge in strArr[(count+1):]:
        x, y, cost = edge.split('-')
        cost = int(cost)
        graph[x][y] = min(graph[x].get(y, cost), cost)
        graph[y][x] = min(graph[y].get(x, cost), cost)
    return graph, strArr[1], strArr[count]
