"""
第一阶段：基础语法速通
目标：快速掌握 Python 基础语法，利用 C++ 基础加速理解
"""

# ==================== 1. 基础数据类型 ====================
print("=== 基础数据类型 ===")
a: int = 10          # 动态类型，但可以加类型注解（Python 3.6+）
b: float = 3.14
c: bool = True        # 注意大写 T/F
d: str = "Hello"
e: None = None        # None 是 NoneType 的唯一值

# type() 查看类型
print(type(a), type(b), type(d))  # <class 'int'> <class 'float'> <class 'str'>

# ==================== 2. 字符串与 f-string ====================
print("\n=== 字符串 ===")
name = "世界"
print(f"Hello, {name}!")          # f-string（Python 3.6+）
print("Hello, {}!".format(name))   # str.format()
print("Hello, %s!" % name)         # 旧式格式化

# 常用字符串方法
s = "  hello, world!  "
print(s.strip())                   # 去除首尾空白 -> "hello, world!"
print(s.split(","))                # 分割 -> ["  hello", " world!  "]
print(",".join(["a", "b", "c"]))   # 连接 -> "a,b,c"
print(s.replace("world", "Python"))# 替换
print(s.find("world"))             # 查找索引 -> 8
print("hello" in s)                # 成员检查 -> True

# 切片（重要！面试高频）
arr = [0, 1, 2, 3, 4, 5]
print(arr[1:4])     # [1, 2, 3]
print(arr[:3])      # [0, 1, 2]
print(arr[3:])      # [3, 4, 5]
print(arr[::-1])    # 反转 -> [5, 4, 3, 2, 1, 0]
print(arr[::2])     # 步长为2 -> [0, 2, 4]
print(arr[:-1])     # 去掉最后一个 -> [0, 1, 2, 3, 4]

# ==================== 3. 控制流 ====================
print("\n=== 控制流 ===")

# if-elif-else（注意：Python 没有 switch）
score = 85
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "D"
print(f"Grade: {grade}")

# for 循环（面试重点：enumerate / zip / range）
print("\n-- for 循环 --")
# enumerate：同时获取 index 和 value
for i, v in enumerate(["a", "b", "c"]):
    print(f"index={i}, value={v}")

# zip：并行迭代
names = ["Alice", "Bob", "Charlie"]
scores = [85, 92, 78]
for name, score in zip(names, scores):
    print(f"{name}: {score}")

# range
for i in range(5):       # 0,1,2,3,4
    pass
for i in range(2, 6):    # 2,3,4,5
    pass
for i in range(0, 10, 2):# 0,2,4,6,8
    pass

# for-else（Python 特色！循环正常结束才执行 else）
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            break
    else:  # 没有找到因子 -> 质数
        print(f"{n} 是质数")

# ==================== 4. 列表推导式（面试必考！） ====================
print("\n=== 列表推导式 ===")

# 基本形式：[expression for item in iterable if condition]
squares = [x**2 for x in range(10)]
print(f"平方列表: {squares}")

# 带条件
evens = [x for x in range(20) if x % 2 == 0]
print(f"偶数: {evens}")

# 嵌套推导式（展平二维列表）
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [num for row in matrix for num in row]
print(f"展平: {flattened}")

# 字典推导式
square_dict = {x: x**2 for x in range(5)}
print(f"字典推导式: {square_dict}")

# 集合推导式
unique = {x % 3 for x in range(10)}
print(f"集合推导式: {unique}")

# ==================== 5. 函数与参数 ====================
print("\n=== 函数 ===")

# 默认参数（注意：默认参数必须是不可变对象！）
def add(a, b=0):
    return a + b

# *args 收集多余位置参数 -> 元组
def sum_all(*args):
    return sum(args)

print(sum_all(1, 2, 3, 4))  # 10

# **kwargs 收集关键字参数 -> 字典
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Alice", age=25, city="北京")

# 拆包（解包）
def func(a, b, c):
    print(a, b, c)

args = (1, 2, 3)
func(*args)          # 元组拆包

kwargs = {"a": 10, "b": 20, "c": 30}
func(**kwargs)       # 字典拆包

# 多返回值（本质是元组）
def min_max(arr):
    return min(arr), max(arr)

minimum, maximum = min_max([3, 1, 4, 1, 5, 9])
print(f"min={minimum}, max={maximum}")

# ==================== 6. lambda 表达式 ====================
print("\n=== lambda ===")

# lambda 参数: 表达式
square = lambda x: x ** 2
print(square(5))  # 25

# 排序时常用 key
students = [("Alice", 85), ("Bob", 92), ("Charlie", 78)]
sorted_by_score = sorted(students, key=lambda x: x[1], reverse=True)
print(f"按成绩排序: {sorted_by_score}")

# map / filter（列表推导式通常更 Pythonic）
nums = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, nums))
evens_filtered = list(filter(lambda x: x % 2 == 0, nums))
print(f"map 翻倍: {doubled}")
print(f"filter 偶数: {evens_filtered}")

# 列表推导式等效写法（更推荐）
print(f"[x*2 for x]: {[x*2 for x in nums]}")
print(f"[x for x if]: {[x for x in nums if x % 2 == 0]}")

# ==================== 7. 常用内置函数 ====================
print("\n=== 内置函数 ===")

# any / all
print(any([False, True, False]))   # True
print(all([True, True, False]))    # False

# sorted（返回新列表，原列表不变）
print(sorted([3, 1, 4, 1, 5]))     # [1, 1, 3, 4, 5]
print(sorted("hello"))             # ['e', 'h', 'l', 'l', 'o']

# enumerate（面试高频）
for i, ch in enumerate("abcd", start=1):  # start 指定起始值
    print(f"第{i}个字符: {ch}")

# zip（面试高频）
keys = ["name", "age", "city"]
values = ["Alice", 25, "北京"]
print(dict(zip(keys, values)))  # 构建字典
