from faker import Faker
import pytest
from faker_procurex.providers.trade_name.zh_CN import Provider

fake = Faker("zh_CN")
fake.add_provider(Provider)

def test_readename():
    # 修改: 使用 assert 来验证测试结果，而不是 print
    product_name = fake.product_name()
    print(product_name)
    assert isinstance(product_name, str), "生成的商品名称应为字符串类型"
    assert product_name.strip(), "生成的商品名称不应为空字符串"
    print(f"生成的商品名称: {product_name}")  # 可选: 保留打印语句以便调试