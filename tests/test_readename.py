from faker import Faker
import pytest
from faker_procurex.providers.trade_name.zh_CN import Provider

fake = Faker("zh_CN")
fake.add_provider(Provider)

def test_readename():
    # 修改: 使用 assert 来验证测试结果，而不是 print
    product_name = fake.product_name()
    assert isinstance(product_name, str), "生成的商品名称应为字符串类型"
    assert product_name.strip(), "生成的商品名称不应为空字符串"
    print(f"\n生成的商品名称: {product_name}")  # 可选: 保留打印语句以便调试

def test_random_city_data():
    city_data = fake.get_random_city_data()
    assert isinstance(city_data, str), "生成的城市数据应为字符串类型"
    assert city_data.strip(), "生成的城市数据不应为空字符串"
    print(f"\n生成的城市数据: {city_data}")

if __name__ == "__main__":
    pytest.main([__file__])
    