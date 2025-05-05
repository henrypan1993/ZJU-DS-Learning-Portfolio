# 一元多项式求和及求积

def read_data():

    nums = list(map(int, input().split()))
    n = nums[0]
    poly = {}
    for i in range(1, 2*n, 2):
        coef, exp = nums[i], nums[i+1]
        poly[exp] = coef
    return poly

def add_poly(poly1, poly2):

    result = poly1.copy()  # 使用copy()函数，避免修改原多项式

    for exp, coef in poly2.items():
        if exp in result:
            # 如果指数相同，则系数相加
            result[exp] += coef
            # 如果系数相加后为0，删除该项
            if result[exp] == 0:
                del result[exp]
        else:
            # 如果指数不同，则加一个新的项
            result[exp] = coef

    return result

def multiply_poly(poly1, poly2):

    result = {}

    # 遍历两个字典
    for exp1, coef1 in poly1.items():
        for exp2, coef2 in poly2.items():
            
            # 计算新项的指数和系数
            new_exp = exp1 + exp2 # n^m做乘法运算时，是将两个指数相加
            new_coef = coef1 * coef2 # 两个系数相乘

            # 将结果保存到对应的指数位置
            if new_exp in result:  # 如果指数已经存在，则相加
                result[new_exp] += new_coef
            else:  # 如果指数不存在，则直接赋值
                result[new_exp] = new_coef

    # 删除系数为0的项
    result = {exp: coef for exp, coef in result.items() if coef != 0}

    return result

def print_poly(poly):
    # 如果多项式为空，输出零多项式
    if not poly:
        print("0 0")
        return

    # 将多项式按指数从高到低排序
    sorted_poly = sorted(poly.items(), key=lambda x: x[0], reverse=True)

    # 构建输出字符串
    result = []
    for exp, coef in sorted_poly:
        # 只输出非零系数项
        if coef != 0:
            result.append(f"{coef} {exp}")
    
    # 连接所有项，用空格分隔 (这部分应该在循环外)
    output = " ".join(result)
    
    # 如果所有项都被移除(所有系数都为0)
    if not output:
        print("0 0")
    else:
        print(output)
    

def main():

    # 1. 已知数据分两行输入，则构建两个一元多项式
    poly1, poly2 = read_data(), read_data()    

    # 2. 设计一个加法函数，求两个一元多项式的和
    poly_sum = add_poly(poly1, poly2)

    # 3. 设计一个乘法函数，求两个一元多项式的积
    poly_product = multiply_poly(poly1, poly2)
    
    # 4. 设计输出函数，将一元多项式输出为标准形式
    print_poly(poly_sum)
    print_poly(poly_product)

main()