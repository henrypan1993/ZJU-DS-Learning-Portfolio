# 02-线性结构4 Pop Sequence

def is_valid_pop_sequence(M, N, pop_sequence):
    """
    判断给定的出栈序列是否有效
    :param M: 栈的最大容量
    :param N: 入栈序列的最大长度
    :param pop_sequence: 需要验证的出栈顺序
    :return: YES if the sequence is valid or NO otherwise
    """
    stack = []  # 定义一个栈
    push_num = 1  # 入栈的值从1开始

    for num in pop_sequence:
        # 如果当前栈顶的数字不是目标数字，则开始入栈
        while (not stack or stack[-1] != num) and push_num <= N:
            stack.append(push_num)
            push_num += 1
            # 检查栈是否溢出
            if len(stack) > M:
                return "NO"  # 栈溢出代表当前序列不可能

        # 如果当前栈顶的数字就是目标数字，则将其弹出
        if stack and stack[-1] == num:
            stack.pop()
        else:
            return "NO"  # 处理有可能找不到这个数字的情况，如N为5，出栈值为6

    # 如果所有的数字都处理完
    return "YES"  # 出栈序列是有效的


def main():
    # 接收输入数据,注意第一行输入的是三个端点值
    first_line = input().strip().split()  # 用空格分开
    M = int(first_line[0])  # 栈的最大容量
    N = int(first_line[1])  # 入栈序列的最大长度
    K = int(first_line[2])  # 待测试的序列数量

    # 处理之后每一行的测试序列
    for i in range(K):
        pop_sequence = list(map(int, input().strip().split()))
        print(is_valid_pop_sequence(M, N, pop_sequence))


if __name__ == "__main__":
    main()