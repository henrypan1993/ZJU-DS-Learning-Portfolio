from collections import defaultdict, deque

def dfs(graph, start, visited):

    """
    采用深度优先方法，从给定的位置开始遍历未访问过的结点
    """

    connected_list = []
    stack = [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            connected_list.append(vertex)
            # 通过排序实现按编号递增的顺序访问邻接点,由于栈后进先出，所以要降序
            stack.extend(sorted(graph[vertex], reverse=True))
    return connected_list

def bfs(graph, start, visited):

    """
    采用广度优先方法，从给定的位置开始遍历未访问过的结点
    """

    connected_list = []
    queue = deque([start])
    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            visited.add(vertex)
            connected_list.append(vertex)
            # 通过排序实现按编号递增的顺序访问邻接点,由于队列先进先出，所以要升序
            queue.extend(sorted(graph[vertex]))
    return connected_list


def find_connected_sets(graph, n):

    """
    确保从编号最小的顶点出发，遍历图中所有的结点
    """
    visited_dfs = set()
    visited_bfs = set()
    dfs_list = []
    bfs_list = []
    for i in range(n):
        if i not in visited_dfs:
            dfs_connected_list = dfs(graph, i, visited_dfs)
            dfs_list.append(dfs_connected_list)
        if i not in visited_bfs:
            bfs_connected_list = bfs(graph, i, visited_bfs)
            bfs_list.append(bfs_connected_list)
    return dfs_list, bfs_list

def main():

    # 将输入数据保存为列表
    n, m = map(int, input().split())
    edges = [tuple(map(int, input().split())) for _ in range(m)]

    # 建立图
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)  # 由于是无向图，所以两端各需要保存一次
        graph[v].append(u)
        

    # 查找图中的连通集
    dfs_list, bfs_list = find_connected_sets(graph, n)

    # 结构化输出
    for data in dfs_list:
        print(f"{{ {' '.join(map(str, data))} }}")
    for data in bfs_list:
        print(f"{{ {' '.join(map(str, data))} }}")

if __name__ == "__main__":
    main()
