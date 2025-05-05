class AVLNode:
    def __init__(self, key):
        self.key = key
        self.height = 1
        self.left = None
        self.right = None

def height(node):
    if not node:
        return 0
    return node.height

def get_balance(node):
    if not node:
        return 0
    return height(node.left) - height(node.right)

def update_height(node):
    if not node:
        return
    node.height = max(height(node.left), height(node.right)) + 1

def right_rotate(y):
    x = y.left
    T2 = x.right
    
    # 执行旋转
    x.right = y
    y.left = T2
    
    # 更新高度
    update_height(y)
    update_height(x)
    
    # 返回新的根节点
    return x

def left_rotate(x):
    y = x.right
    T2 = y.left
    
    # 执行旋转
    y.left = x
    x.right = T2
    
    # 更新高度
    update_height(x)
    update_height(y)
    
    # 返回新的根节点
    return y

def insert(root, key):
    # 标准BST插入
    if not root:
        return AVLNode(key)
    
    if key < root.key:
        root.left = insert(root.left, key)
    elif key > root.key:
        root.right = insert(root.right, key)
    else:  # 键值已存在，AVL树不允许重复
        return root
    
    # 更新当前节点的高度
    update_height(root)
    
    # 获取平衡因子
    balance = get_balance(root)
    
    # 如果不平衡，则执行旋转
    
    # 左左情况
    if balance > 1 and key < root.left.key:
        return right_rotate(root)
    
    # 右右情况
    if balance < -1 and key > root.right.key:
        return left_rotate(root)
    
    # 左右情况
    if balance > 1 and key > root.left.key:
        root.left = left_rotate(root.left)
        return right_rotate(root)
    
    # 右左情况
    if balance < -1 and key < root.right.key:
        root.right = right_rotate(root.right)
        return left_rotate(root)
    
    # 返回未变更的节点指针
    return root

def main():
    n = int(input())
    keys = list(map(int, input().split()))
    
    root = None
    for key in keys:
        root = insert(root, key)
    
    print(root.key)

if __name__ == "__main__":
    main() 