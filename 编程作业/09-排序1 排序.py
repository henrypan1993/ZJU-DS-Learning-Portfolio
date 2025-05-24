import heapq

# 冒泡排序
def bubble_sort(nums):

    """
    :param nums: 待排序列。
    :return: 返回排好的序列。
    """
    n = len(nums)
    for i in range(n):
        for j in range(0, n - i -1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]

    return nums

# 插入排序
def insertion_sort(nums):

    """
    :param nums: 待排序列。
    :return: 返回排好的序列。
    """
    for i in range(1, len(nums)):
        key = nums[i]
        j = i - 1
        while j >= 0 and key < nums[j]:
            nums[j + 1] = nums[j]
            j = j - 1
        nums[j + 1] = key

    return nums

# 希尔排序
def shell_sort(nums):

    """
    :param nums: 待排序列。
    :return: 返回排好的序列。
    """
    n = len(nums)
    gap = n // 2 # 初始步长

    while gap > 0:
        for i in range(gap, n):
            temp = nums[i]
            j = i
            # 对每个步长进行排序
            while j >= gap and nums[j - gap] > temp:
                nums[j] = nums[j - gap] # 后移元素
                j -= gap # 按步长回退
            nums[j] = temp
        gap = gap // 2 # 减小步长
    
    return nums


# 堆排序
def heap_sort(nums):

    """
    :param nums: 待排序列。
    :return: 返回排好的序列。
    """    
    # 构建最小堆
    heapq.heapify(nums)  # 原地转换为最小堆，时间复杂度O(N)

    # 逐个弹出最小元素
    sorted_nums = []
    while nums:
        sorted_nums.append(heapq.heappop(nums))

    # 将排序后的结果复制回原数组
    nums[:] = sorted_nums # 用新的内容替换当前列表的所有元素
    return nums

# 归并排序：递归实现    
def merge_sort_recursive(nums):

    """
    :param nums: 待排序列。
    :return: 返回排好的序列。
    """
    if len(nums) <= 1:
        return nums
    
    mid = len(nums) // 2
    left = merge_sort_recursive(nums[:mid])
    right = merge_sort_recursive(nums[mid:])
    
    return merge(left, right)

def merge(left, right):

    """
    :param left: 左半部分，已排序。
    :param right: 右半部分，已排序。
    :return: 返回合并后的序列。
    """
    result = []
    while left and right:
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    
    # 处理剩余元素
    result.extend(left)
    result.extend(right)
    return result

# 归并排序：非递归实现
def merge_sort_iterative(nums):

    """
    :param nums: 待排序列。
    :return: 返回排好的序列。
    """    
    n = len(nums)
    # 初始步长为1
    step = 1
    while step < n:
        for i in range(0, n, step * 2):
            left = nums[i:i + step] # 左半部分
            right = nums[i + step:i + step * 2] # 右半部分
            nums[i:i + step * 2] = merge(left, right) # 合并
        step *= 2
    
    return nums


def main():

    # 处理输入
    n = int(input())
    nums = list(map(int, input().split()))

    # 利用内置库函数排序
    # nums.sort()

    # 冒泡排序
    # bubble_sort(nums)

    # 插入排序
    # insertion_sort(nums)

    # 希尔排序
    # shell_sort(nums)

    # 堆排序
    # heap_sort(nums)

    # 归并排序：递归实现
    # nums = merge_sort_recursive(nums)

    # 归并排序：非递归实现
    merge_sort_iterative(nums)

    # 输出
    print(' '.join(map(str, nums)))

if __name__ == '__main__':
    main()
