from collections import defaultdict, deque


def dfs(graph, start, visited):
    connected_set = []
    stack = [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            connected_set.append(vertex)
            # 按编号递增顺序访问邻接点
            stack.extend(sorted(graph[vertex], reverse=True))
    return connected_set


def bfs(graph, start, visited):
    connected_set = []
    queue = deque([start])
    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            visited.add(vertex)
            connected_set.append(vertex)
            # 按编号递增顺序访问邻接点
            queue.extend(sorted(graph[vertex]))
    return connected_set


def find_connected_sets(graph, n):
    visited = set()
    dfs_sets = []
    bfs_sets = []
    for i in range(n):
        if i not in visited:
            dfs_connected_set = dfs(graph, i, visited.copy())
            dfs_sets.append(dfs_connected_set)
            bfs_connected_set = bfs(graph, i, visited.copy())
            bfs_sets.append(bfs_connected_set)
    return dfs_sets, bfs_sets


# 示例用法
n = 5
m = 3
edges = [(0, 1), (1, 2), (3, 4)]
graph = defaultdict(list)
for u, v in edges:
    graph[u].append(v)
    graph[v].append(u)

dfs_sets, bfs_sets = find_connected_sets(graph, n)
print("DFS Connected Sets:", dfs_sets)
print("BFS Connected Sets:", bfs_sets)