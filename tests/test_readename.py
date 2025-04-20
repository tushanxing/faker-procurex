from faker import Faker
import pytest
import asyncio
import time
from faker_procurex.providers.trade_name.zh_CN.random_city import Provider

fake = Faker("zh_CN")
fake.add_provider(Provider)


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



def test_random_city_data():

    city_data = fake.get_random_city_data()
    assert isinstance(city_data, str), "生成的城市数据应为字符串类型"
    assert city_data.strip(), "生成的城市数据不应为空字符串"
    print(f"\n生成的城市数据: {city_data}")

if __name__ == "__main__":
    pytest.main([__file__])
    