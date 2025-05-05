def init_graph(n, m):
    """
    初始化图

    Args:
        n: 节点数
        m: 边数

    Returns:
        graph: 邻接矩阵
    """
    graph = [[float('inf')] * n for _ in range(n)] # 初始化一个 n x n 的距离矩阵
    for i in range(n):
        graph[i][i] = 0  # 节点到自身的距离为0
    for _ in range(m):
        u, v, w = map(int, input().split())
        # 处理输入值和邻接表中对应的值有偏移的情况
        u = u - 1
        v = v - 1
        graph[u][v] = w # 无向图，所以需要设置两个方向的边
        graph[v][u] = w
    return graph  # 返回初始化好的图


def find_min_max_distance(graph, n):
    """
    寻找最大距离的最小节点

    Args:
        graph: 邻接矩阵
        n: 节点数
    """
    # Floyd算法求解任意两点之间的最短路径
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if graph[i][j] > graph[i][k] + graph[k][j]:
                    graph[i][j] = graph[i][k] + graph[k][j]
    
    # 寻找最大距离的最小节点
    min_max_distance = float('inf')
    min_node = -1
    for i in range(n):
        max_dist = 0
        possible = True
        for j in range(n):
            if i!=j and graph[i][j] == float('inf'):
                possible = False
                break
            if graph[i][j] > max_dist:
                max_dist = graph[i][j]
        if possible and max_dist < min_max_distance:
            min_max_distance = max_dist
            min_node = i + 1 # 节点编号从1开始
        elif possible and max_dist == min_max_distance:
            min_node = min(min_node, i + 1)
    
    return min_node, min_max_distance
            

def main():

    # 处理输入数据
    n, m = map(int, input().split())
    graph = init_graph(n, m)

    # 寻找最大距离的最小节点
    min_node, min_max_distance = find_min_max_distance(graph, n)

    # 输出结果
    if min_node == -1:
        print("0")
    else:
        print(min_node, min_max_distance)

if __name__ == "__main__":
    main()
