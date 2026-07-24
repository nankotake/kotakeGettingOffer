"""
第四阶段：高级特性与精通之路
涵盖：并发与异步、元编程、内存管理、类型注解、测试
"""

# ==================== 1. 线程与进程 ====================
print("=" * 60)
print("=== 并发编程 ===")
print("=" * 60)

from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor, as_completed
import threading
import time


def io_bound_task(n):
    """模拟IO密集型任务"""
    time.sleep(1)
    return n * n


def thread_pool_example():
    """线程池（IO密集型任务适用）"""
    with ThreadPoolExecutor(max_workers=4) as executor:
        futures = [executor.submit(io_bound_task, i) for i in range(8)]
        for future in as_completed(futures):
            print(f"线程池结果: {future.result()}")


# 线程安全问题演示
class Counter:
    def __init__(self):
        self.value = 0
        self.lock = threading.Lock()

    def increment(self):
        with self.lock:  # 加锁保证线程安全
            self.value += 1

    def increment_without_lock(self):
        self.value += 1  # 线程不安全


counter = Counter()


def unsafe_increment():
    for _ in range(100000):
        counter.increment_without_lock()


# 如果不加锁，结果很可能不是 300000
threads = [threading.Thread(target=unsafe_increment) for _ in range(3)]
for t in threads:
    t.start()
for t in threads:
    t.join()
print(f"不加锁结果（预期300000，实际可能小于）: {counter.value}")


# ==================== 2. asyncio 异步编程 ====================
print("\n" + "=" * 60)
print("=== asyncio 异步编程 ===")
print("=" * 60)

import asyncio


async def fetch_data(delay, name):
    """模拟异步IO操作"""
    print(f"开始获取 {name}...")
    await asyncio.sleep(delay)  # 模拟异步等待，不阻塞事件循环
    print(f"{name} 完成")
    return f"{name} 的数据"


async def async_main():
    # 同时执行多个协程
    tasks = [
        fetch_data(2, "API-1"),
        fetch_data(1, "API-2"),
        fetch_data(3, "API-3"),
    ]
    results = await asyncio.gather(*tasks)
    print(f"所有结果: {results}")


# 运行异步代码
# asyncio.run(async_main())  # 取消注释即可运行


# ==================== 3. 元编程 ====================
print("\n" + "=" * 60)
print("=== 元编程 ===")
print("=" * 60)


# 3.1 type() 动态创建类
def init(self, name):
    self.name = name


def greet(self):
    return f"Hello, I'm {self.name}"


DynamicPerson = type('DynamicPerson', (object,), {
    '__init__': init,
    'greet': greet,
    'species': 'Human'
})

p = DynamicPerson("Alice")
print(f"动态创建的类: {p.greet()}, species={p.species}")


# 3.2 元类
class SingletonMeta(type):
    """单例元类"""
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


class Singleton(metaclass=SingletonMeta):
    def __init__(self):
        self.value = 0


s1 = Singleton()
s2 = Singleton()
print(f"单例模式: s1 is s2 = {s1 is s2}")  # True


# 3.3 __slots__ 优化内存
class WithSlots:
    """使用 __slots__ 减少内存占用"""
    __slots__ = ('x', 'y')

    def __init__(self, x, y):
        self.x = x
        self.y = y
        # self.z = 0  # 会报错！__slots__ 限制了属性


class WithoutSlots:
    def __init__(self, x, y):
        self.x = x
        self.y = y


import sys
obj1 = WithSlots(1, 2)
obj2 = WithoutSlots(1, 2)
print(f"WithSlots 大小: {sys.getsizeof(obj1)}")
print(f"WithoutSlots 大小: {sys.getsizeof(obj2)}")


# ==================== 4. 深浅拷贝 ====================
print("\n" + "=" * 60)
print("=== 深浅拷贝（面试必考）===")
print("=" * 60)

import copy

original = {
    'name': 'Alice',
    'scores': [85, 92, 78],
    'info': {'age': 25, 'city': '北京'}
}

# 浅拷贝：只拷贝最外层，内层引用共享
shallow = copy.copy(original)
shallow['scores'].append(100)  # 会影响 original！
shallow['info']['age'] = 30   # 会影响 original！

print(f"原始: {original}")
print(f"浅拷贝: {shallow}")

# 深拷贝：完全独立的拷贝
original2 = {
    'name': 'Alice',
    'scores': [85, 92, 78],
}
deep = copy.deepcopy(original2)
deep['scores'].append(100)
print(f"原始2: {original2}")  # 不受影响
print(f"深拷贝: {deep}")

# is vs ==（面试必考）
a = [1, 2, 3]
b = [1, 2, 3]
c = a
print(f"a == b: {a == b}")   # True，值相等
print(f"a is b: {a is b}")   # False，不同对象
print(f"a is c: {a is c}")   # True，同一对象


# ==================== 5. 类型注解 ====================
print("\n" + "=" * 60)
print("=== 类型注解（Type Hints）===")
print("=" * 60)

from typing import List, Dict, Optional, Tuple, Callable, TypeVar, Generic


def process_items(items: List[str]) -> Dict[str, int]:
    """类型注解示例"""
    result: Dict[str, int] = {}
    for item in items:
        result[item] = len(item)
    return result


def find_user(user_id: int) -> Optional[str]:
    """可能返回 None 的情况"""
    users = {1: "Alice", 2: "Bob"}
    return users.get(user_id)


# Callable：函数类型注解
def apply_twice(func: Callable[[int], int], x: int) -> int:
    return func(func(x))


# 泛型（Generics）
T = TypeVar('T')


class Stack(Generic[T]):
    """泛型栈"""
    def __init__(self):
        self.items: List[T] = []

    def push(self, item: T) -> None:
        self.items.append(item)

    def pop(self) -> T:
        return self.items.pop()


int_stack = Stack[int]()
int_stack.push(1)
int_stack.push(2)
print(f"泛型栈弹出: {int_stack.pop()}")


# dataclasses：数据类
from dataclasses import dataclass


@dataclass
class Point:
    x: float
    y: float

    def distance_from_origin(self) -> float:
        return (self.x ** 2 + self.y ** 2) ** 0.5


p = Point(3.0, 4.0)
print(f"Point: {p}, 距离原点: {p.distance_from_origin()}")
# dataclass 自动生成了 __init__, __repr__, __eq__ 等


# ==================== 6. 面试陷阱题 ====================
print("\n" + "=" * 60)
print("=== Python 面试陷阱题 ===")
print("=" * 60)


# 6.1 默认参数陷阱
def append_to(element, target=[]):  # 默认参数在函数定义时只计算一次！
    target.append(element)
    return target


print(f"第一次: {append_to(1)}")   # [1]
print(f"第二次: {append_to(2)}")   # [1, 2] ！不是 [2]
# 正确做法：target=None，内部 if target is None: target = []


# 6.2 闭包延迟绑定
def create_multipliers():
    """闭包陷阱"""
    return [lambda x: i * x for i in range(5)]


multipliers = create_multipliers()
print([m(2) for m in multipliers])  # [8, 8, 8, 8, 8] 不是 [0, 2, 4, 6, 8]！
# 原因：闭包捕获的是变量 i 的引用，循环结束时 i=4
# 修正：lambda x, i=i: i * x


# 6.3 可变对象作为默认值
def add_student(name, students=[]):
    students.append(name)
    return students


class1 = add_student("Alice")
class2 = add_student("Bob")
print(f"class1: {class1}")  # ['Alice', 'Bob'] —— Alice 还在！
print(f"class2: {class2}")  # ['Alice', 'Bob']


# 6.4 字符串驻留（面试冷门）
a = "hello_world"
b = "hello_world"
print(f"短字符串 is: {a is b}")  # True（CPython 驻留机制）

a2 = "hello_world_!" * 10
b2 = "hello_world_!" * 10
print(f"长字符串 is: {a2 is b2}")  # True or False（取决于实现）


# 6.5 变量作用域（LEGB 规则）
x = "global"


def outer():
    x = "outer"

    def inner():
        x = "inner"
        print(f"inner: {x}")

    inner()
    print(f"outer: {x}")


outer()
print(f"global: {x}")

# nonlocal 用法
def counter_maker():
    count = 0

    def increment():
        nonlocal count  # 引用外层函数的变量
        count += 1
        return count

    return increment


counter = counter_maker()
print(f"counter: {counter()}, {counter()}, {counter()}")  # 1, 2, 3
