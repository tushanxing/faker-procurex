import os
import orjson
import asyncio
import aiofiles
from collections import deque
from concurrent.futures import ThreadPoolExecutor

# 获取当前脚本所在的目录
script_dir = os.path.dirname(os.path.abspath(__file__))
# 构建 data.json 文件的相对路径
datapath = os.path.join(script_dir, "city_data.json")

# 缓存加载的 JSON 数据
cached_data = None


async def load_json_from_file(file_path=datapath):
    """从文件加载 JSON 数据"""
    global cached_data
    if cached_data is not None:
        return cached_data
    try:
        async with aiofiles.open(file_path, "rb") as f:
            content = await f.read()
            data = orjson.loads(content)
            cached_data = data
            return data
    except FileNotFoundError:
        print(f"文件未找到: {file_path}")
        return None
    except orjson.JSONDecodeError as e:
        print(f"JSON 解析错误: {e}")
        return None


def _extract_full_paths_sync(node=None, current_path=""):
    # 如果传入的节点为空，返回空列表
    if node is None:
        return []

    # 初始化路径列表和栈，栈中存储节点和当前路径
    paths = []
    stack = deque([(node, current_path)])

    # 当栈不为空时，继续处理
    while stack:
        # 从栈中取出一个节点和当前路径
        node, current_path = stack.popleft()
        # 如果节点是字典类型
        if isinstance(node, dict):
            # 遍历字典的键值对
            for key, value in node.items():
                # 构建新的路径，如果当前路径不为空，则在当前路径后添加键，否则直接使用键
                new_path = f"{current_path}{key}" if current_path else key
                # 将值和新的路径入栈
                stack.append((value, new_path))
        # 如果节点是列表类型
        elif isinstance(node, list):
            # 遍历列表中的每个元素
            for item in node:
                # 如果元素是字符串类型，则直接将当前路径和元素拼接后添加到路径列表中
                if isinstance(item, str):
                    paths.append(f"{current_path}{item}")
                # 如果元素不是字符串类型，则将其和当前路径入栈
                else:
                    stack.append((item, current_path))
        # 如果节点既不是字典也不是列表
        else:
            # 将当前路径和节点的字符串形式拼接后添加到路径列表中
            paths.append(current_path + str(node))

    return paths


# 定义一个异步函数 extract_full_paths_sync，用于从 JSON 文件中提取完整路径
async def extract_full_paths_sync():
    # 获取当前正在运行的 asyncio 事件循环
    loop = asyncio.get_running_loop()
    # 异步调用 load_json_from_file 函数，从文件中加载 JSON 数据
    node = await load_json_from_file()
    # 如果加载的 JSON 数据为空（即 node 为 None），则返回一个空列表
    if node is None:
        return []
    # 使用 ThreadPoolExecutor 创建一个线程池执行器
    with ThreadPoolExecutor() as executor:
        # 使用事件循环的 run_in_executor 方法，在线程池中执行 _extract_full_paths_sync 函数
        # 该函数用于同步地提取 JSON 数据中的完整路径
        result = await loop.run_in_executor(executor, _extract_full_paths_sync, node)
    # 返回提取的完整路径结果
    return result


def extract_full_paths():
    return asyncio.run(extract_full_paths_sync())


# 使用示例：
if __name__ == "__main__":
    # 提取所有完整路径
    result = extract_full_paths()
    print(result)
