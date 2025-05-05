# 02-线性结构3 Reversing Linked List

def get_data():

    fisrt_addr, N, K = input().split() # 获取第一行数据，即首地址、节点总数和组数
    N, K = int(N), int(K)

    nodes = {}

    # 从第二行开始的数据结构为Address Data Next，所以用循环处理
    for _ in range(N):
        addr, data, next_addr = input().split()
        nodes[addr] = [data, next_addr]

    return fisrt_addr, nodes, K

def build_list(fisrt_addr, nodes):

    linked_list = []
    addr = fisrt_addr

    while addr != "-1": # 题目中用-1表示null
        linked_list.append(addr)
        addr = nodes[addr][1] # 获取下一个节点的地址
    return linked_list

def reverse_list(linked_list, K):

    for i in range(0, len(linked_list) - len(linked_list) % K, K):
        linked_list[i:i+K] = linked_list[i:i+K][::-1]

    return linked_list

def print_list(linked_list, nodes):

    # 检查链表是否为空
    if not linked_list:
        print("-1")
        return

    for i in range(len(linked_list) -1):
        print(f"{linked_list[i]} {nodes[linked_list[i]][0]} {linked_list[i+1]}")

    print(f"{linked_list[-1]} {nodes[linked_list[-1]][0]} -1") # 按照题目要求，最后一个节点输出后没有下一个节点，输出-1表示指针指向null

def main():

    # 读取数据
    fisrt_addr, nodes, K = get_data()

    # 构建链表
    linked_list = build_list(fisrt_addr, nodes)

    # 分组反转
    linked_list = reverse_list(linked_list, K)

    # 输出结果
    print_list(linked_list, nodes)

if __name__ == "__main__":
    main()