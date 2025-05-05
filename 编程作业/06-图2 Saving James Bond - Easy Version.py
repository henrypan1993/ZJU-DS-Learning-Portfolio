import math

def first_jump(distance, isle_r, locations_croc):

    """
    当Bond站在小岛中心时，尝试往岛外跳跃。

    :param locations_croc: 所有鳄鱼的位置。
    :param isle_r: 表示小岛的半径。
    :param distance: 表示最大跳跃距离的数值。
    :return: 返回起点坐标的列表，如果没有可以跳的位置就返回空列表。
    """

    start = []
    for x,y in locations_croc:
         # 判断鳄鱼是否在Bond从岛上可跳到的范围内
        if math.sqrt(x*x + y*y) <= isle_r + distance: 
            start.append((x, y))
            
    return start

def DFS(location, vertex, distance, visited=None):
    """
    当Bond已经跳上了鳄鱼的脑袋，尝试跳上岸。递归实现深度优先搜索。
    
    :param location: Bond当前所在的位置坐标。
    :param vertex: 所有鳄鱼的位置列表。
    :param distance: 表示最大跳跃距离的数值。
    :param visited: 已访问的位置集合。
    :return: 如果可以跳上岸返回 True，否则返回 False。
    """
    # 初始化visited集合
    if visited is None:
        visited = set()
    
    # 如果当前位置可以直接跳上岸，返回True
    if is_safe(location, distance):
        return True
    
    # 标记当前位置为已访问
    visited.add(location)
    
    # 递归探索所有可能的下一步位置
    for next_pos in vertex:
        # 如果该位置没有被访问过且可以从当前位置跳到
        if next_pos not in visited and jump_nearby(distance, location, next_pos):
            # 递归探索从next_pos出发的路径
            if DFS(next_pos, vertex, distance, visited):
                return True
    
    # 所有可能的路径都无法到达岸边
    return False

def is_safe(location, distance):

    """
    判断当前位置是否可以跳上岸。

    :param location: 包含 x 和 y 坐标的可迭代对象（如元组或列表），表示当前位置。
    :param distance: 表示最大跳跃距离的数值。
    :return: 如果可以跳上岸返回 True，否则返回 False。
    """

    x, y = location

    if x + 50 <= distance or 50 - x <= distance:
        return True
    elif y + 50 <= distance or 50 - y <= distance:
        return True
    else:
        return False

def jump_nearby(distance, v, w):

    """
    判断是否能够跳上邻近的鳄鱼。

    :param v: 当前Bond所在的位置。
    :param w: 邻近的一条鳄鱼的位置。
    :param distance: 表示最大跳跃距离的数值。
    :return: 如果可以跳上鳄鱼返回 True，否则返回 False。
    """

    if math.sqrt((v[0] - w[0])**2 + (v[1] - w[1])**2) <= distance:
        return True
    else:
        return False

def main():

    # 处理输入数据
    num_croc, D = map(int, input().split())
    locations_croc = [tuple(map(int, input().split())) for _ in range(num_croc)]
    radius = 15 / 2 # 根据题意：The central island is a disk centered at (0,0) with the diameter of 15

    # 首次跳跃
    loc_of_Bond = first_jump(D, radius, locations_croc)

    # 如果已经踩在了鳄鱼脑袋上，就继续跳跃
    result = False # 默认Bond逃不出去
    if loc_of_Bond:
        for loc in loc_of_Bond: # 注意存在多个起点
            if DFS(loc, locations_croc, D): # 传递正确的参数
                result = True
                break
    
    # 给出最终判断
    print("Yes" if result else "No")

if __name__ == "__main__":
    main()