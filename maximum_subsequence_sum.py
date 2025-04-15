# 01-复杂度2 Maximum Subsequence Sum

def max_subarray_sum(n, array):
    current_sum = 0
    max_sum = -float('inf')  # 初始化为负无穷大
    start = 0
    end = n-1  # 默认为整个数组
    temp_start = 0


    # 记录第一个0的位置（如果存在）
    first_zero = -1
    for i in range(n):
        if array[i] == 0:
            first_zero = i
            break


    for i in range(n):
        # 决定是继续当前子列还是开始新的子列
        if current_sum + array[i] < 0:
            current_sum = 0
            temp_start = i + 1  # 下一个位置开始新的子序列
        else:
            current_sum += array[i]
            
            # 如果当前和大于最大和，或者当前和等于最大和但起始位置更靠前
            if (current_sum > max_sum) or (current_sum == max_sum and temp_start < start):
                max_sum = current_sum
                start = temp_start
                end = i
    
    # 如果最大和仍为负无穷大，说明全是负数
    if max_sum < 0:
        return 0, array[0], array[n-1]
    
    # 如果最大和为0，且存在0元素，返回第一个0
    if max_sum == 0 and first_zero != -1:
        return 0, array[first_zero], array[first_zero]
        
    return max_sum, array[start], array[end]


n = int(input())
array = list(map(int, input().split())) # 将输入字符串分割并转换为整数列表
    
max_sum, start, end = max_subarray_sum(n, array)
print(f"{max_sum} {start} {end}")