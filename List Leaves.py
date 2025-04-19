from collections import deque

class TreeNode:
    def __init__(self):
        self.left = None
        self.right = None
        self.value = None

def build_tree(node_count):
    """
    Args:
        node_count: 树的节点数量
    Returns:
        TreeNode: 树的根节点
    Raises:
        ValueError: 当无法确定唯一的根结点时
    """
    # 存储所有结点
    nodes = {}
    # 存储被引用的结点索引
    referenced_indics = set()

    # 首先创建所有节点
    for i in range(node_count):
        nodes[i] = TreeNode()
        nodes[i].value = i

    # 建立节点之间的连接
    for i in range(node_count):
        left_idx, right_idx = input().strip().split()
        
        if left_idx != "-":
            left_idx = int(left_idx)
            nodes[i].left = nodes[left_idx]
            referenced_indics.add(left_idx)
            
        if right_idx != "-":
            right_idx = int(right_idx)
            nodes[i].right = nodes[right_idx]
            referenced_indics.add(right_idx)

    # 查找根结点
    root_index = [i for i in range(node_count) if i not in referenced_indics]
    if len(root_index) != 1:
        raise ValueError("无法确定唯一的根结点")

    return nodes[root_index[0]]

def level_order_traversal(root):
    """
    Args:
        root: 树的根结点
    Returns:
        List: 存放叶子结点值的列表
    """
    if not root:
        return []
    
    queue = deque([root])
    list_leaves = []

    while queue:
        node = queue.popleft()

        if node.left is None and node.right is None:
            list_leaves.append(str(node.value))

        if node.left is not None:
            queue.append(node.left)
        if node.right is not None:
            queue.append(node.right)
    
    return list_leaves

def main():
    # 根据输入值"种树"
    nodes = int(input())  # 第一行将输入结点个数
    tree = build_tree(nodes)

    # 使用层序遍历获取叶子结点的位置
    leaves = level_order_traversal(tree)

    # 结构化输出
    if leaves:
        print(" ".join(leaves))
    else:
        print("-1")
    
if __name__ == "__main__":
    main()