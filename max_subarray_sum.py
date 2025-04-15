# 01-复杂度1 最大子列和问题

def max_subarray_sum(n, array):

    current_sum = 0
    max_sum = 0

    for i in range(n):
        
        # 决定是继续当前子列还是以新元素重新开始
        current_sum = max(array[i], current_sum + array[i])

        # 更新最大子列和
        max_sum = max(max_sum, current_sum)

    return max_sum if max_sum > 0 else 0 # 如果结果为负，则直接返回0

n = int(input())  # 将输入转换为整数
array = list(map(int, input().split()))  # 将输入字符串分割并转换为整数列表

print(max_subarray_sum(n, array))