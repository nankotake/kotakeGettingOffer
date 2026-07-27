"""
第二阶段：进阶特性（面试高频考点）
涵盖：装饰器、生成器、迭代器、面向对象、上下文管理器
"""

from functools import wraps
import time


# ==================== 1. 装饰器（面试必考！） ====================
print("=" * 50)
print("=== 装饰器 ===")
print("=" * 50)


# 1.1 最简单的装饰器
def simple_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"调用函数前: {func.__name__}")
        result = func(*args, **kwargs)
        print(f"调用函数后，结果: {result}")
        return result
    return wrapper


@simple_decorator
def greet(name):
    return f"Hello, {name}"


greet("Alice")  # 相当于 simple_decorator(greet)("Alice")

# 1.2 使用 functools.wraps（保留原函数元信息）
def timer_decorator(func):
    @wraps(func)  # 保留 func 的 __name__, __doc__ 等属性
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        elapsed = time.time() - start
        print(f"{func.__name__} 耗时: {elapsed:.4f}s")
        return result
    return wrapper


@timer_decorator
def slow_function():
    time.sleep(0.1)
    return "Done"


slow_function()
print(f"函数名保留: {slow_function.__name__}")  # 没有 wraps 会变成 'wrapper'


# 1.3 带参数的装饰器
def repeat(n: int):
    """装饰器工厂：重复执行 n 次"""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(n):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator


@repeat(3)
def say_hi(name):
    print(f"Hi, {name}")
    return name


say_hi("Bob")  # 会打印 3 次


# 1.4 类装饰器
class CountCalls:
    def __init__(self, func):
        self.func = func
        self.count = 0

    def __call__(self, *args, **kwargs):
        self.count += 1
        print(f"{self.func.__name__} 被调用了 {self.count} 次")
        return self.func(*args, **kwargs)


@CountCalls
def hello():
    print("Hello!")


hello()
hello()
print(f"总调用次数: {hello.count}")


# 1.5 实战：实现一个简单的缓存装饰器（类似 lru_cache）
def memoize(func):
    cache = {}

    @wraps(func)
    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrapper


@memoize
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


print(f"fibonacci(30) = {fibonacci(30)}")  # 很快，因为有缓存


# ==================== 2. 生成器与迭代器 ====================
print("\n" + "=" * 50)
print("=== 生成器与迭代器 ===")
print("=" * 50)


# 2.1 生成器函数（使用 yield）
def fibonacci_generator():
    """斐波那契数列生成器（面试高频）"""
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


fib = fibonacci_generator()
print([next(fib) for _ in range(10)])  # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]


# 2.2 生成器表达式（惰性求值，节省内存）
# 列表推导式：立即生成所有元素
list_squares = [x ** 2 for x in range(10)]  # 占用内存
# 生成器表达式：按需生成
gen_squares = (x ** 2 for x in range(10))    # 几乎不占内存
print(f"列表推导式: {list_squares}")
print(f"生成器表达式: {list(gen_squares)}")

# 2.3 yield from（Python 3.3+）
def chain(*iterables):
    """连接多个可迭代对象"""
    for it in iterables:
        yield from it  # 等价于 for x in it: yield x


print(list(chain([1, 2, 3], "abc", range(3))))  # [1, 2, 3, 'a', 'b', 'c', 0, 1, 2]

# 2.4 自定义迭代器
class CountDown:
    """倒计时迭代器"""
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        self.current -= 1
        return self.current + 1


for num in CountDown(5):
    print(num, end=" ")  # 5 4 3 2 1
print()


# ==================== 3. 面向对象编程 ====================
print("\n" + "=" * 50)
print("=== 面向对象编程 ===")
print("=" * 50)


# 3.1 类与魔术方法
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        """调试用，返回对象的官方表示"""
        return f"Vector({self.x}, {self.y})"

    def __str__(self):
        """用户友好表示"""
        return f"({self.x}, {self.y})"

    def __add__(self, other):
        """支持 + 运算符"""
        return Vector(self.x + other.x, self.y + other.y)

    def __eq__(self, other):
        """支持 == 比较"""
        return self.x == other.x and self.y == other.y

    def __len__(self):
        """支持 len()"""
        return 2

    def __getitem__(self, index):
        """支持索引访问 v[0], v[1]"""
        if index == 0:
            return self.x
        elif index == 1:
            return self.y
        raise IndexError

    def __call__(self, scale):
        """让实例可调用 v(2)"""
        return Vector(self.x * scale, self.y * scale)


v1 = Vector(1, 2)
v2 = Vector(3, 4)
print(f"v1 = {v1}")
print(f"v1 + v2 = {v1 + v2}")
print(f"v1 == Vector(1, 2): {v1 == Vector(1, 2)}")
print(f"len(v1) = {len(v1)}")
print(f"v1[0] = {v1[0]}, v1[1] = {v1[1]}")
print(f"v1(3) = {v1(3)}")  # __call__


# 3.2 @property 属性装饰器
class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError("半径不能为负")
        self._radius = value

    @property
    def area(self):
        return 3.14159 * self._radius ** 2

    @property
    def diameter(self):
        return self._radius * 2


c = Circle(5)
print(f"半径: {c.radius}, 面积: {c.area:.2f}, 直径: {c.diameter}")
c.radius = 10  # 使用 setter
# c.radius = -1  # 会抛出 ValueError


# 3.3 @classmethod vs @staticmethod
class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    @classmethod
    def from_string(cls, date_str):
        """类方法：通过字符串创建实例"""
        year, month, day = map(int, date_str.split("-"))
        return cls(year, month, day)

    @staticmethod
    def is_valid_date(date_str):
        """静态方法：验证日期格式，不需要类或实例"""
        try:
            year, month, day = map(int, date_str.split("-"))
            return 1 <= month <= 12 and 1 <= day <= 31
        except:
            return False

    def __repr__(self):
        return f"Date({self.year}, {self.month}, {self.day})"


d = Date.from_string("2024-03-15")
print(f"类方法创建: {d}")
print(f"验证日期: {Date.is_valid_date('2024-13-01')}")  # False


# ==================== 4. 上下文管理器 ====================
print("\n" + "=" * 50)
print("=== 上下文管理器 ===")
print("=" * 50)


# 4.1 类方式实现
class FileManager:
    def __init__(self, filename, mode='r'):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()
        # 返回 False 会传播异常，True 会抑制异常
        return False


# 4.2 装饰器方式实现（更简洁）
from contextlib import contextmanager


@contextmanager
def timer():
    """计时器上下文管理器（面试高频）"""
    start = time.time()
    try:
        yield  # yield 之前的代码在 __enter__ 执行，之后的在 __exit__ 执行
    finally:
        elapsed = time.time() - start
        print(f"耗时: {elapsed:.4f}s")


with timer():
    time.sleep(0.2)
    print("执行了一些操作...")


# ==================== 5. functools 与 itertools ====================
print("\n" + "=" * 50)
print("=== functools & itertools ===")
print("=" * 50)

from functools import partial
from itertools import chain, permutations, combinations, product, groupby

# partial：固定部分参数
def power(base, exp):
    return base ** exp


square = partial(power, exp=2)
cube = partial(power, exp=3)
print(f"5的平方: {square(5)}")
print(f"5的立方: {cube(5)}")

# itertools.permutations：排列
print(list(permutations([1, 2, 3], 2)))  # [(1,2), (1,3), (2,1), (2,3), (3,1), (3,2)]

# itertools.combinations：组合
print(list(combinations([1, 2, 3], 2)))  # [(1,2), (1,3), (2,3)]

# itertools.product：笛卡尔积
print(list(product([1, 2], ['a', 'b'])))  # [(1,'a'), (1,'b'), (2,'a'), (2,'b')]

# itertools.groupby：分组（需要先排序）
data = [("A", 1), ("A", 2), ("B", 3), ("B", 4)]
for key, group in groupby(data, key=lambda x: x[0]):
    print(f"{key}: {list(group)}")

# @lru_cache：函数结果缓存

from functools import lru_cache

@lru_cache(maxsize=128)
def expensive_func(n):
    """模拟耗时计算"""
    time.sleep(0.05)
    return n * n


print("首次计算（会慢）:", expensive_func(10))
print("缓存命中（会快）:", expensive_func(10))
