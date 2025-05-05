class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = TreeNode(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = TreeNode(value)
            else:
                self._insert_recursive(node.left, value)
        else:
            if node.right is None:
                node.right = TreeNode(value)
            else:
                self._insert_recursive(node.right, value)


def is_same_tree(tree1, tree2):
    if tree1 is None and tree2 is None:
        return True
    if tree1 is None or tree2 is None:
        return False
    if tree1.value != tree2.value:
        return False
    return is_same_tree(tree1.left, tree2.left) and is_same_tree(tree1.right, tree2.right)

def is_same_bst(seq1, seq2):
    # 创建两棵树
    tree1 = BinarySearchTree()
    tree2 = BinarySearchTree()
    
    # 按照给定的序列插入节点
    for value in seq1:
        tree1.insert(value)
    
    for value in seq2:
        tree2.insert(value)
    
    # 比较两棵树是否相同
    return is_same_tree(tree1.root, tree2.root)

def main():
    while True:
        first_line = input().strip().split()
        
        # 检查输入是否只有一个数字0
        if len(first_line) == 1 and int(first_line[0]) == 0:
            break
            
        n, l = int(first_line[0]), int(first_line[1])
        
        # 读取初始序列
        initial_seq = list(map(int, input().strip().split()))
        
        # 处理每个需要检查的序列
        for _ in range(l):
            test_seq = list(map(int, input().strip().split()))
            
            # 判断测试序列与初始序列是否生成相同的BST
            if is_same_bst(initial_seq, test_seq):
                print("Yes")
            else:
                print("No")

if __name__ == "__main__":
    main()
