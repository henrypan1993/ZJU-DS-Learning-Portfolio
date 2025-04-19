class TreeNode:
    """树的节点类"""
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def build_tree(node_count):
    """
    根据输入构建树结构
    Args:
        node_count: 树的节点数量
    Returns:
        TreeNode: 树的根节点
    Raises:
        ValueError: 当输入格式不正确或无法构建有效的树时
    """
    if node_count <= 0:
        return None

    # 存储所有节点
    nodes = {}
    # 记录被引用的节点索引
    referenced_indices = set()
    # 存储节点连接信息
    connections = []

    # 读取并验证节点信息
    for i in range(node_count):
        try:
            value, left_idx, right_idx = input().strip().split()
            nodes[i] = TreeNode(value)
            connections.append((left_idx, right_idx))
            
            # 记录被引用的节点
            if left_idx != "-":
                referenced_indices.add(int(left_idx))
            if right_idx != "-":
                referenced_indices.add(int(right_idx))
        except ValueError:
            raise ValueError(f"第{i+1}行输入格式错误")

    # 建立节点之间的连接
    for i in range(node_count):
        left_idx, right_idx = connections[i]
        if left_idx != "-":
            try:
                nodes[i].left = nodes[int(left_idx)]
            except (ValueError, KeyError):
                raise ValueError(f"无效的左子节点索引: {left_idx}")
        if right_idx != "-":
            try:
                nodes[i].right = nodes[int(right_idx)]
            except (ValueError, KeyError):
                raise ValueError(f"无效的右子节点索引: {right_idx}")

    # 查找根节点（没有被引用的节点）
    root_indices = [i for i in range(node_count) if i not in referenced_indices]
    if len(root_indices) != 1:
        raise ValueError("无法确定唯一的根节点")

    return nodes[root_indices[0]]

def is_isomorphic(tree1, tree2):
    """
    判断两棵树是否同构
    Args:
        tree1: 第一棵树的根节点
        tree2: 第二棵树的根节点
    Returns:
        bool: 如果两棵树同构返回True，否则返回False
    """
    # 两棵树都为空
    if tree1 is None and tree2 is None:
        return True
    
    # 只有一棵树为空
    if tree1 is None or tree2 is None:
        return False
    
    # 根节点值不同
    if tree1.value != tree2.value:
        return False
    
    # 检查两种情况：
    # 1. 不交换左右子树
    # 2. 交换左右子树
    return (is_isomorphic(tree1.left, tree2.left) and 
            is_isomorphic(tree1.right, tree2.right)) or \
           (is_isomorphic(tree1.left, tree2.right) and 
            is_isomorphic(tree1.right, tree2.left))

def main():
    """主函数"""
    try:
        # 读取并构建第一棵树
        n1 = int(input())
        tree1 = build_tree(n1)
        
        # 读取并构建第二棵树
        n2 = int(input())
        tree2 = build_tree(n2)
        
        # 判断是否同构并输出结果
        result = is_isomorphic(tree1, tree2)
        print("Yes" if result else "No")
        
    except ValueError as e:
        print(f"输入错误: {e}")
    except Exception as e:
        print(f"程序运行出错: {e}")

if __name__ == "__main__":
    main()
