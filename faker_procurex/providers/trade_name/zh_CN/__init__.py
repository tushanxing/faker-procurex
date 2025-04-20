import cProfile
import asyncio
import pstats
import time

def profile(func):
    def wrapper(*args, **kwargs):
        # 创建一个 Profile 对象
        profiler = cProfile.Profile()
        # 使用 Profile 对象的 enable() 方法开始分析
        profiler.enable()
        # 调用函数
        result = func(*args, **kwargs)
        # 使用 Profile 对象的 disable() 方法停止分析
        profiler.disable()
        # 创建一个 Stats 对象并输出分析结果
        stats = pstats.Stats(profiler).sort_stats('cumulative')
        stats.print_stats()
        return result
    return wrapper

def timer_decorator(func):
    async def async_wrapper(*args, **kwargs):
        start_time = time.time()
        result = await func(*args, **kwargs)
        end_time = time.time()
        name_time = end_time - start_time
        print(f"{func.__name__}: 执行时间: {name_time:.6f} 秒")
        return result

    def sync_wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        name_time = end_time - start_time
        print(f"{func.__name__}: 执行时间: {name_time:.6f} 秒")
        return result

    if asyncio.iscoroutinefunction(func):
        return async_wrapper
    return sync_wrapper