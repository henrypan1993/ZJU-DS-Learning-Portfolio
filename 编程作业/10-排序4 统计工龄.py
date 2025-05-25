def bucket_sort(ages):
    """
    使用桶排序算法对工龄进行统计
    
    Args:
        ages: 工龄列表
    """
    # 初始化计数数组，工龄范围0~50
    count = [0] * 51
    
    # 统计每个工龄的出现次数
    for age in ages:
        count[age] += 1
    
    # 输出每个工龄的统计结果
    for i in range(51):
        if count[i] > 0:
            print(f"{i}:{count[i]}")

def main():
    """
    主函数：处理输入并输出统计结果
    """
    # 处理输入
    n = int(input())
    ages = list(map(int, input().split()))

    # 统计工龄
    bucket_sort(ages)

if __name__ == "__main__":
    main()
