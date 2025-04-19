from faker.providers import BaseProvider
from typing import Union, List, Dict
import random
from faker import Faker

PRODUCTTYPE: Dict[str, list] = {
    "食品": ["面包", "饼干", "糖果", "巧克力", "牛奶", "果汁", "咖啡", "茶", "酒", "零食"],
    "服装": ["T恤", "牛仔裤", "衬衫", "连衣裙", "运动鞋", "高跟鞋", "帽子", "围巾", "手套", "袜子"],
    "电子产品": ["智能手机", "平板电脑", "笔记本电脑", "电视", "音响", "游戏机", "相机", "耳机", "鼠标", "键盘"],
    "家居用品": ["床", "沙发", "餐桌", "椅子", "柜子", "灯具", "窗帘", "地毯", "收纳盒", "餐具"],
    "化妆品": ["口红", "粉底", "睫毛膏", "香水", "面霜", "洗发水", "沐浴露", "防晒霜", "睫毛夹", "化妆刷"],
    "书籍": ["小说", "传记", "历史", "科学", "哲学", "艺术", "旅游", "教育", "儿童", "杂志"],
    "玩具": ["积木", "拼图", "娃娃", "模型", "遥控车", "球类", "户外玩具", "益智玩具", "儿童图书", "儿童服装"],
    "运动器材": ["篮球", "足球", "网球", "羽毛球", "游泳装备", "健身器材", "瑜伽垫", "运动鞋", "运动服", "运动配件"],
    "宠物用品": ["狗粮", "猫粮", "宠物玩具", "宠物窝", "宠物医疗", "宠物美容", "宠物服装", "宠物食品", "宠物清洁", "宠物饰品"],
    "汽车配件": ["轮胎", "机油", "刹车片", "雨刷", "导航仪", "行车记录仪", "座垫", "方向盘套", "脚垫", "车载冰箱"],
    "办公用品": ["打印机", "复印机", "传真机", "扫描仪", "计算器", "文具", "文件夹", "笔记本", "白板", "办公桌"],
    "家具": ["沙发", "餐桌", "椅子", "床", "衣柜", "书架", "茶几", "电视柜", "餐桌椅", "鞋柜"],
    "家电": ["空调", "洗衣机", "冰箱", "电视", "热水器", "微波炉", "烤箱", "洗碗机", "烤箱", "咖啡机"],
    "数码产品": ["智能手机", "平板电脑", "笔记本电脑", "相机", "耳机", "鼠标", "键盘", "游戏机", "智能手表", "智能手环"]
}


city_cascade_data: Dict[str, Dict[str, Dict[str, Dict[str, List[str]]]]] = {
    "四川省": {
        "成都市": {
            "锦江区": {
                "春熙路街道": ["东村", "西村", "南村", "北村"],
                "镋钯街街道": ["中村", "前村", "后村"],
                "牛市口街道": ["左村", "右村", "中村"]
            },
            "青羊区": {
                "少城街道": ["小村", "大村", "新村"],
                "草市街道": ["旧村", "新村", "幸福村"],
                "黄田坝街道": ["田村", "坝村", "黄村"]
            },
            "金牛区": {
                "抚琴街道": ["琴村", "抚村", "琴坝村"],
                "茶店子街道": ["茶村", "店村", "子村"],
                "天回镇街道": ["天村", "回村", "镇村"]
            }
        },
        "绵阳市": {
            "涪城区": {
                "青义镇": ["义村", "青村", "义坝村"],
                "龙门镇": ["龙门村", "龙村", "门村"],
                "杨家镇": ["杨村", "家村", "杨坝村"]
            },
            "游仙区": {
                "小枧镇": ["枧村", "小村", "枧坝村"],
                "魏城镇": ["魏村", "城村", "魏坝村"],
                "石马镇": ["石村", "马村", "石坝村"]
            },
            "安州区": {
                "花荄镇": ["花村", "荄村", "花坝村"],
                "塔水镇": ["塔村", "水村", "塔坝村"],
                "桑枣镇": ["桑村", "枣村", "桑坝村"]
            }
        }
    }
}


class Provider(BaseProvider):
    """
    生成商品名称
    """
    def product_name(self) -> str:
        """
        生成商品名称
        :return: 商品名称
        """
        # 修复：将 {} 替换为 []，并确保括号匹配
        category = self.random_element(list(PRODUCTTYPE.keys()))
        product_name = self.random_element(PRODUCTTYPE[category])
        return product_name

    def get_random_city_data(self) -> str:
        """
        随机获取一个国家及其行政区域的城市数据
        :return: 包含国家、行政区域、城市和村庄的字符串
        """
        # 随机选择一个国家
        country = self.random_element(list(city_cascade_data.keys()))
        
        # 随机选择一个行政区域
        province = self.random_element(list(city_cascade_data[country].keys()))
        
        # 随机选择一个城市
        city = self.random_element(list(city_cascade_data[country][province].keys()))
        
        # 随机选择一个街道
        street = self.random_element(list(city_cascade_data[country][province][city].keys()))
        
        # 随机选择一个村庄
        village = self.random_element(city_cascade_data[country][province][city][street])
        
        # 拼接字符串
        return f"{country}{province}{city}{street}{village}"


if __name__ == "__main__":
    # 使用 Faker 初始化 Provider
    fake = Faker()
    provider = Provider(fake)
    print(provider.get_random_city_data())  # 获取随机城市数据
    # print(provider.product_name())  # 获取随机商品名称