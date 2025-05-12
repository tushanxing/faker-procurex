from faker.providers import BaseProvider
from faker import Faker
from faker_procurex.service.readate.read_data import extract_full_paths
import asyncio
import numpy as np

# 加载所有路径
all_locations = np.array(extract_full_paths())

async def get_random_index():
    # 确保生成的索引在有效范围内
    # print(len(all_locations))
    return np.random.randint(0, 620573)


class Provider(BaseProvider):  # 定义一个名为Provider的类，继承自BaseProvider基类
    async def get_random_city_data_sync(self) -> str:  # 定义一个异步方法，用于获取随机的城市数据，返回类型为字符串
        index = await get_random_index()  # 调用异步函数get_random_index获取一个随机索引
        return all_locations[index]  # 返回all_locations列表中对应索引的城市数据

    def get_random_city_data(self):  # 定义一个同步方法，用于获取随机的城市数据
        return asyncio.run(self.get_random_city_data_sync())  # 使用asyncio.run运行异步方法get_random_city_data_sync，并返回结果


if __name__ == "__main__":
    fake = Faker()
    provider = Provider(fake)
    result = provider.get_random_city_data()
    print(result)
