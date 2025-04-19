def insert_heap(heap, value):
    """向最小堆中插入一个新值
    
    Args:
        heap: 当前堆
        value: 要插入的值
    """
    heap.append(value)
    sift_up(heap, len(heap) - 1)


def sift_up(heap, i):
    """上浮操作，维护最小堆性质
    
    Args:
        heap: 当前堆
        i: 要上浮的节点索引
    """
    while i > 0:
        parent = (i - 1) // 2
        if heap[i] >= heap[parent]:
            break
        heap[i], heap[parent] = heap[parent], heap[i]
        i = parent


def build_min_heap(nums):
    """从数组构建最小堆
    
    Args:
        nums: 输入数组
    
    Returns:
        构建好的最小堆
    """
    heap = []
    for num in nums:
        insert_heap(heap, num)
    return heap


def get_path_to_root(heap, index):
    """获取从指定节点到根节点的路径
    
    Args:
        heap: 当前堆
        index: 节点索引(0-indexed)
    
    Returns:
        从当前节点到根节点的路径(字符串形式)
    """
    path = []
    node = index
    while node >= 0:
        path.append(str(heap[node]))
        if node == 0:  # 到达根节点
            break
        node = (node - 1) // 2
    return " ".join(path)


def process_queries(heap, queries):
    """处理所有查询
    
    Args:
        heap: 当前堆
        queries: 查询索引列表(1-indexed)
    """
    for k in queries:
        # 将1-indexed转换为0-indexed
        index = k - 1
        
        # 检查索引是否有效
        if index < 0 or index >= len(heap):
            print(f"索引 {k} 超出范围")
            continue
        
        # 输出从当前节点到根节点的路径
        print(get_path_to_root(heap, index))


def main():
    """主函数，处理输入和输出"""
    # 读取输入
    n, m = map(int, input().split())
    nums = list(map(int, input().split()))[:n]
    queries = list(map(int, input().split()))[:m]
    
    # 建立最小堆
    heap = build_min_heap(nums)
    
    # 处理查询
    process_queries(heap, queries)


if __name__ == "__main__":
    main() 