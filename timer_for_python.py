import time

def function_timer(func): # 装饰器函数，用于计算函数执行时间

    def wrapper(*args, **kwargs): # 包装器函数，用于接收函数参数

        start_time = time.time() # 获取函数开始执行时间
        result = func(*args, **kwargs) # 运行函数
        end_time = time.time()
        print(f"函数{func.__name__}执行时间：{end_time - start_time}秒")
        return result # 返回函数结果

    return wrapper