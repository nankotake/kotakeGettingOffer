"""
第一阶段：基础语法速通
目标：快速掌握 Python 基础语法，利用 C++ 基础加速理解
"""

# ==================== 1. 基础数据类型 ====================
import heapq


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

# ==================== 8. 集合 set（非常重要！） ====================
print("\n=== 集合 set ===")

# 集合是无序的、不重复的元素集合，底层用哈希表实现，O(1) 查找
# 类似 C++ 的 unordered_set

# 8.1 创建集合
empty_set = set()           # 空集合（注意：{} 是空字典！）
numbers = {1, 2, 3, 4, 5}
print(f"集合: {numbers}")

# 从列表创建集合（去重 — 面试高频！）
dup_list = [1, 2, 2, 3, 3, 3, 4]
unique = set(dup_list)
print(f"列表去重: {unique}")           # {1, 2, 3, 4}
print(f"转回列表: {list(unique)}")     # 但顺序不一定保持

# 8.2 集合推导式
squares_set = {x**2 for x in range(5)}
print(f"集合推导式: {squares_set}")    # {0, 1, 4, 9, 16}

# 8.3 基本操作（增删查）
s = {1, 2, 3}
s.add(4)                # 添加元素
print(f"add(4): {s}")

s.remove(2)             # 删除元素（不存在会抛 KeyError）
print(f"remove(2): {s}")

s.discard(10)           # 安全删除（不存在也不会报错）
x = s.pop()             # 随机弹出一个元素并返回
print(f"pop: {x}, 剩余: {s}")

s.clear()               # 清空集合
print(f"clear后: {s}")

# 8.4 成员检查（O(1) 效率，面试高频！）
fruits = {"apple", "banana", "orange", "grape"}
print(f"'apple' in set: {'apple' in fruits}")    # True
print(f"'watermelon' not in set: {'watermelon' not in fruits}")  # True

# vs 列表查找（列表是 O(n)，集合是 O(1)）
big_list = list(range(1000000))
big_set = set(range(1000000))
import time

start = time.time()
print(999999 in big_list)   # 列表查找
print(f"列表查找耗时: {time.time() - start:.4f}s")

start = time.time()
print(999999 in big_set)    # 集合查找
print(f"集合查找耗时: {time.time() - start:.4f}s")

# 8.5 集合运算（面试必考！）
a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}

# 并集（Union）：a ∪ b
print(f"并集 a | b: {a | b}")           # {1,2,3,4,5,6,7,8}
print(f"union(): {a.union(b)}")

# 交集（Intersection）：a ∩ b
print(f"交集 a & b: {a & b}")           # {4,5}
print(f"intersection(): {a.intersection(b)}")

# 差集（Difference）：a - b（在 a 中但不在 b 中的元素）
print(f"差集 a - b: {a - b}")           # {1,2,3}
print(f"difference(): {a.difference(b)}")

# 对称差集（Symmetric Difference）：(a ∪ b) - (a ∩ b)
print(f"对称差集 a ^ b: {a ^ b}")       # {1,2,3,6,7,8}
print(f"symmetric_difference(): {a.symmetric_difference(b)}")

# 8.6 子集 / 超集判断
x = {1, 2, 3}
y = {1, 2, 3, 4, 5}
print(f"x ⊆ y: {x.issubset(y)}")       # True
print(f"y ⊇ x: {y.issuperset(x)}")     # True
print(f"是否不相交: {x.isdisjoint({6, 7})}")  # True

# 8.7 frozenset（不可变集合，可作为字典的键）
frozen = frozenset([1, 2, 3])
# frozen.add(4)  # 会报错！frozenset 不可变
d = {frozen: "这是一个不可变集合的键"}
print(f"frozenset作为字典键: {d}")

# 8.8 集合实战面试题
print("\n--- 集合实战 ---")

# 题1：两个数组的交集（LeetCode 349）
def intersection(nums1, nums2):
    return list(set(nums1) & set(nums2))

print(f"数组交集: {intersection([1,2,2,1], [2,2])}")  # [2]

# 题2：找数组中唯一的元素（其他元素都出现两次）
def single_number(nums):
    return list(set(nums))  # 仅演示，实际找唯一要用异或

# 题3：字符串中不同字符的数量
def count_unique_chars(s):
    return len(set(s))

print(f"不同字符数 'hello': {count_unique_chars('hello')}")  # 4 (h,e,l,o)

# 题4：判断两个字符串是否是字母异位词（anagram）
def is_anagram(s1, s2):
    return set(s1) == set(s2) and len(s1) == len(s2)
    # 更精确应该用 Counter，但集合可以快速判断

# 题5：列表中是否有重复元素（面试高频）
def has_duplicate(nums):
    return len(nums) != len(set(nums))

print(f"[1,2,3,1] 有重复: {has_duplicate([1,2,3,1])}")  # True
print(f"[1,2,3] 有重复: {has_duplicate([1,2,3])}")     # False
