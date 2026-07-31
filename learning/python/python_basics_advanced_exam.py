"""
=============================================================================
Python 面试笔试 - 基础语法 & 高级特性 专项练习卷 (含自动判卷)
=============================================================================
考试说明:
  - 本卷聚焦 Stage 1 (基础语法) 和 Stage 2 (高级特性), 共 42 题, 满分 100 分
  - 请在每道题目的答案区域填写你的代码/答案
  - 写完直接 python 运行本文件即自动判卷评分
  - 标记 [MANUAL] 的题为概念题, 需人工对照参考答案, 不计入自动评分
=============================================================================
"""

from functools import wraps, reduce, partial
from typing import Any
from itertools import chain, product, groupby, islice, permutations, combinations
from collections import deque, Counter, ChainMap
from contextlib import contextmanager
from abc import ABC, abstractmethod
import time
import copy
import math


# =============================================================================
# 第 1 节：数据类型基础 (6分)
# =============================================================================

# Q1 (2分)  - Python 有哪些不可变类型？请用列表列举至少 4 种。
q1_answer = ["int","float","str","tuple","frozenset","bool","bytes"]  # <-- 列表

# Q2 (2分) [MANUAL] - 解释下面两行输出什么及原因:
#   a = 256; b = 256; print(a is b)
#   a = 257; b = 257; print(a is b)
# 你的答案用注释写在这里即可.
# 都是YES
# 256在python里有小整数优化，用的是同一个内存地址
# 257是因为在同一行赋值


# Q3 (2分) [MANUAL] - None 的类型是什么？和 "" / [] / 0 在布尔上下文中的异同？
# 你的答案用注释写在这里即可.
# NoneType, 在布尔上下文都是False，但是None在对比的时候只能用is，其他用==，而且None不能计算


# =============================================================================
# 第 2 节：字符串操作 (6分)
# =============================================================================

# Q4 (2分) - 对 s = "  Hello, World!  " 做: 去首尾空白 / 全小写 / 全大写 / 首字母大写
s4 = "  Hello, World!  "
q4_a = s4.strip()   # <-- 字符串
q4_b = s4.lower()   # <-- 字符串
q4_c = s4.upper()   # <-- 字符串
q4_d = s4.capitalize()   # <-- 字符串

# Q5 (2分) - f-string 格式化: 名字 "Alice", 年龄 25, pi 取 3 位小数
q5_name = "Alice"
q5_age = 25
q5_result = f"{q5_name} is {q5_age} years old, pi = {math.pi:.3f}"  # <-- 字符串

# Q6 (2分) - join/split: ["a","b","c"] 用逗号连接, 再切回列表
q6_a = ",".join(["a","b","c"])
q6_b = q6_a.split(",")

# =============================================================================
# 第 3 节：控制流与循环技巧 (8分)
# =============================================================================

# Q7 (2分) - 用 for-else 找出 2~20 之间的所有质数
q7_primes = []  # <-- 列表
for i in range(2,21):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        q7_primes.append(i)


# Q8 (2分) - 用 enumerate + zip 格式化输出
# 给定以下数据:
names_q8 = ["Alice", "Bob", "Charlie"]
scores_q8 = [85, 92, 78]
# 请用 enumerate 和 zip 分别生成如下格式的三行字符串:
#   "1st: Alice got 85"
#   "2nd: Bob got 92"
#   "3rd: Charlie got 78"
nth = [f"{i}{'th' if 10 <= i % 100 <= 20 else {1: 'st', 2: 'nd', 3: 'rd'}.get(i % 10, 'th')}" for i in range(1, 100)]
q8_enumerate_lines = []  # <-- 列表
for i,name in enumerate(names_q8):
    q8_enumerate_lines.append(f"{nth[i]}: {name} got {scores_q8[i]}")
q8_zip_lines = []        # <-- 列表
for name,score in zip(names_q8, scores_q8):
    q8_zip_lines.append(f"{nth[names_q8.index(name)]}: {name} got {score}")
q8_enumerate_and_zip_lines = []
for i, (name, score) in enumerate(zip(names_q8,scores_q8)):
    q8_enumerate_and_zip_lines.append(f"{nth[i]}: {name} got {score}")

# Q9 (2分) - range(10, 0, -1) 和 range(0, 10, 3) 分别产生什么？
q9_range1 = [10,9,8,7,6,5,4,3,2,1]  # <-- 列表
q9_range2 = [0,3,6,9]  # <-- 列表

# Q10 (2分) - 字典模拟 switch, 操作 a=10, b=5
# 给定输入:
a_q10 = 10
b_q10 = 5
# 请用字典映射实现: "+" -> 加法, "-" -> 减法, "*" -> 乘法, "/" -> 除法
# 将包含四个运算结果的字典赋给 q10_dispatch
# 示例格式: q10_dispatch = {"+": 15, "-": 5, "*": 50, "/": 2}
q10_dispatch = {
    "+":a_q10+b_q10,
    "-":a_q10-b_q10,
    "*":a_q10*b_q10,
    "/":a_q10/b_q10
}  # <-- 字典


# =============================================================================
# 第 4 节：切片操作 (6分)
# =============================================================================

arr_sec4 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Q11 (2分) - 切片取: 前5 / 后5 / 索引2~7步长2 / 反转 / 隔一取一
q11_a = arr_sec4[:5]  # <-- 列表
q11_b = arr_sec4[-5:]  # <-- 列表
q11_c = arr_sec4[2:8:2]  # <-- 列表
q11_d = arr_sec4[::-1]  # <-- 列表
q11_e = arr_sec4[::2]  # <-- 列表

# Q12 (2分) - 在 arr = [1,2,3,4,5] 的索引 2 处原地插入 [10,20]
q12_arr = [1, 2, 3, 4, 5]  # <-- 列表（原地修改）
q12_arr[2:2] = [10,20]  # <-- 在此处原地插入

# Q13 (2分) - 一步反转字符串 "hello"
q13 = "hello"
q13_a = q13[::-1]  # <-- 字符串


# =============================================================================
# 第 5 节：推导式 (10分)
# =============================================================================

# Q14 (3分) - 推导式练习
# (a) 用列表推导式生成 0~9 的平方数: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81] -> 赋给 q14_a
# (b) 从 (a) 的结果中只保留偶数平方: [0, 4, 16, 36, 64] -> 赋给 q14_b
# (c) 用字典推导式生成 {0:0, 1:1, 2:8, 3:27, 4:64} -> 赋给 q14_c
q14_a = [x**2 for x in range(0,10)]      # <-- 列表
q14_b = [x for x in q14_a if x%2 == 0] # <-- 列表
q14_c = {x:x**3 for x in range(0,5)}    # <-- 字典

# Q15 (3分) - 展平 matrix = [[1,2,3],[4,5,6],[7,8,9]] -> [1,2,...,9]
matrix = [[1,2,3],[4,5,6],[7,8,9]]
q15_flattened = [x for y in matrix for x in y]

# Q16 (4分) - 一行推导式生成 2~50 之间所有质数
q16_primes = [x for x in range(2,51) if all(x%y!=0 for y in range(2,x))]


# =============================================================================
# 第 6 节：函数参数与作用域 (8分)
# =============================================================================

# Q17 (2分) - print_all(*args, **kwargs): 分别打印位置参数和关键字参数
def q17_print_all(*args, **kwargs):
    print(f"{args},{kwargs}")
    pass  # <-- 完成此函数

# Q18 (2分) [MANUAL] - 下面代码输出什么？
# x = 10
# def outer(): x=20; def inner(): nonlocal x; x=30; inner(); print("outer:", x)
# outer(); print("global:", x)
q18_outer = 30   # <-- outer: 后面的数字
q18_global = 10  # <-- global: 后面的数字

# Q19 (2分) - 修正可变默认参数陷阱
# 原始代码有 bug:
#   def append_to_list(item, my_list=[]):
#       my_list.append(item)
#       return my_list
# 请写出修正版, 使得每次不传参调用都返回只含当次 item 的列表:
#   append_to_list("a") -> ["a"]
#   append_to_list("b") -> ["b"]
def q19_append_to_list(item, my_list=None):
    if my_list is None:
        return [item]
    else:
        my_list.append(item)
    return my_list

# Q20 (2分) - lambda 练习
# (a) 用 lambda 定义平方函数, 赋给 q20_a: q20_a(5) -> 25
q20_a = lambda x : x**2     # <-- lambda 函数
# (b) 用 sorted + lambda 按字符串长度排序 ["apple","kiwi","banana","pear"]
#     结果应为: ["pear", "kiwi", "apple", "banana"] -> 赋给 q20_b
q20 = ["apple","kiwi","banana","pear"]
q20_b = sorted(q20,key=lambda x:len(x))  # <-- 列表


# =============================================================================
# 第 7 节：内置函数 (6分)
# =============================================================================

# Q21 (2分) [MANUAL] - 解释 any/all, zip, enumerate 的用途
# 用注释写在这里即可.

# Q22 (2分) - map / filter 及等价的列表推导式
# 给定 nums = [1,2,3,4,5]
# (a) 用 map 将每个元素平方 -> 赋给 q22_a (应为 [1,4,9,16,25])
# (b) 用 filter 保留偶数 -> 赋给 q22_b (应为 [2,4])
# (c) 用列表推导式写 (a) 的等价代码 -> 赋给 q22_c
# (d) 用列表推导式写 (b) 的等价代码 -> 赋给 q22_d
nums = [1,2,3,4,5]
q22_a = list(map(lambda x : x**2, nums))    # <-- 列表
q22_b = list(filter(lambda x : x%2 == 0, nums)) # <-- 列表
q22_c = [x**2 for x in nums]   # <-- 列表
q22_d = [x for x in nums if x%2==0]

# Q23 (2分) - sorted 按值降序 {"a":3, "b":1, "c":2}
q23 = {"a":3, "b":1, "c":2}
q23_sorted_by_value = sorted(q23.items(),key=lambda x : x[1])  # <-- 列表


# =============================================================================
# 第 8 节：集合深入 (6分)
# =============================================================================

# Q24 (2分) [MANUAL] - set vs frozenset 区别及 frozenset 的用途
# 用注释写在这里即可.

# Q25 (2分) - 用集合判断 "silent" 和 "listen" 是否是异位词, 说明局限
q25_1 = "silent"
q25_2 = "listen"
q25_a = set(q25_1) == set(q25_2)  # <-- 布尔值
# 局限：无法对一个单词出现多个相同字母的情况对比

# Q26 (2分) - 列表去重并保持原序: [1,2,2,3,3,3,4,4,4,4]
seen = set()
q26 = [1,2,2,3,3,3,4,4,4,4]
q26_a = [x for x in q26 if (x not in seen or seen.add(x))]  # <-- 列表


# =============================================================================
# 第 9 节：装饰器 (10分)
# =============================================================================

# Q27 (3分) - 实现装饰器 @log_call
# 要求：装饰后函数被调用时打印:
#   "Calling <函数名> with args: (...) and kwargs: {...}"
#   函数返回后打印:
#   "<函数名> returned: <返回值>"
# 必须将原返回值正常返回给调用方 (不要吞掉)
# 使用 @wraps 保留原函数元信息
def q27_log_call(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        print(f"Calling {func.__name__} with args: {args} and kwargs: {kwargs}")
        result = func(*args,**kwargs)
        print(f"{func.__name__} returned: {result}")
        return result
    return wrapper

# Q28 (3分) - 实现带参数的装饰器 @timeout(seconds)
# 要求：如果被装饰函数执行时间超过 seconds 秒, 抛出 TimeoutError
# 简化版：用 time.time() 检测即可, 不要求真多线程中断
# 正常执行时返回函数的返回值
def q28_timeout(seconds):
    def decorator(func):
        @wraps(func)
        def wrapper(*args,**kwargs):
            startTime = time.time()
            result = func(*args,**kwargs)
            endTime = time.time()
            if (endTime-startTime)>seconds:
                raise TimeoutError
            return result
        return wrapper
    return decorator

# Q29 (4分) - 实现类装饰器 CountCalls
# 要求：
#   @CountCalls
#   def foo(): ...
#   foo() 后可以通过 foo.count 访问调用次数
#   每次调用时: self.count += 1, 然后调用原函数并返回结果
class CountCalls:
    def __init__(self, func) -> None:
        self.count = 0
        self.func = func
    def __call__(self, *args: Any, **kwds: Any) -> Any:
        self.count+=1
        return self.func(*args,**kwds)


# =============================================================================
# 第 10 节：生成器与迭代器 (8分)
# =============================================================================

# Q30 (4分) - 生成器练习 (3个小任务)
# (a) 用 yield 实现 q30_countdown(n): 从 n 倒数到 1
#     示例: list(q30_countdown(5)) -> [5, 4, 3, 2, 1]
def q30_countdown(n):
    while n >= 1:
        yield n
        n-=1

# (b) 用生成器表达式生成 1~100 中所有 7 的倍数, 赋给 q30_multiples_of_7
q30_multiples_of_7 = [i for i in range(1,101) if i>=7 and i%7==0]  # <-- 生成器表达式

# (c) 用 yield from 实现 q30_my_chain(*iterables), 效果等同于 itertools.chain
#     示例: list(q30_my_chain([1,2], [3,4], [5,6])) -> [1,2,3,4,5,6]
def q30_my_chain(*iterables):
    for i in iterables:
        yield from i

# Q31 (4分) - 手写迭代器类 RangeIterator, 模仿 range(stop)
# 要求：RangeIterator(5) 可被 for 循环正常遍历
#       list(RangeIterator(5)) -> [0, 1, 2, 3, 4]
#       实现 __iter__ 和 __next__ 方法
class RangeIterator:
    def __init__(self,count,start = 0) -> None:
        self.count = count
        self.start = start
    def __iter__(self):
        return self
    def __next__(self):
        if self.start < self.count:
            result = self.start
            self.start+=1
            return result
        else:
            raise StopIteration


# =============================================================================
# 第 11 节：面向对象编程 (12分)
# =============================================================================

# Q32 (4分) - BankAccount 类
# 要求:
#   构造: BankAccount("Alice", 100) -> owner="Alice", balance=100
#   deposit(amount): 存款, 返回当前余额
#   withdraw(amount): 取款, 余额不足抛 ValueError
#   @property owner: 只读, 返回姓名
#   @property balance: 只读, 返回余额 (不能直接 balance=xxx 赋值)
#   __str__: 返回 "BankAccount(Alice, balance=120)"
class BankAccount:
    def __init__(self, owner: str, balance: float) -> None:
        self._owner = owner
        self._balance = balance

    def deposit(self, amount):
        self._balance += amount
        return self._balance

    def withdraw(self, amount):
        if amount > self._balance:
            raise ValueError
        self._balance -= amount

    @property
    def owner(self):
        return self._owner

    @property
    def balance(self):
        return self._balance

    def __str__(self) -> str:
        return f"BankAccount({self._owner}, balance={self._balance})"

# Q33 (4分) - DateUtils 类
# @classmethod from_iso: "2024-12-25" -> 返回 (2024, 12, 25) 元组
# @staticmethod is_leap_year: 判断闰年
#   - 能被4整除但不能被100整除, 或能被400整除
#   - is_leap_year(2000) == True, is_leap_year(1900) == False
class DateUtils:
    @classmethod
    def from_iso(self, iso):
        return tuple(int(iso.split("-")))
    
    @staticmethod
    def is_leap_year(year):
        return (year % 4 == 0 and year%100!=0) or (year%400==0)

# Q34 (4分) [MANUAL] - __str__ vs __repr__ 的区别, 写一个类演示
class StrReprDemo:
    def __str__(self):
        return "this is a demo!"
    def __repr__(self):
        return "StrReprDemo()"
# print的时候有str就用str，没有用repr；str（）触发__str__，repr触发__repr__；str应用户友好，repr应开发者友好


# =============================================================================
# 第 12 节：魔术方法 (8分)
# =============================================================================

# Q35 (4分) - Playlist 类 (包装一个歌曲名列表)
# 构造: Playlist(["a","b","c"]) 保存歌曲列表
# __len__: len(pl) -> 3
# __getitem__: pl[0] -> "a"
# __setitem__: pl[0] = "x" 后 pl[0] -> "x"
# __contains__: "b" in pl -> True
class Playlist:
    def __init__(self,list):
        self.playlist = list
    def __len__(self):
        return len(self.playlist)
    def __getitem__(self,pos):
        if pos >= len(self.playlist):
            raise IndexError
        return self.playlist[pos]
    def __setitem__(self,pos,val):
        if pos >= len(self.playlist):
            self.playlist.append(val)
        else:
            self.playlist[pos] = val
    def __contains__(self, val):
        return val in self.playlist

# Q36 (4分) - 实现 Multiplier 类
# 构造: Multiplier(3) -> factor=3
# __call__: 让实例可调用, Multiplier(3)(5) -> 15
# 示例: m = Multiplier(2); m(100) -> 200
class Multiplier:
    def __init__(self,x):
        self.x = x
    def __call__(self,y):
        return self.x*y


# =============================================================================
# 第 13 节：上下文管理器 (6分)
# =============================================================================

# Q37 (3分) - Timer 上下文管理器 (类方式)
# 进入 with 块时记录开始时间 (time.time())
# 退出 with 块时打印耗时, 格式: "耗时: X.XXXXs"
# 用法: with Timer():
#           ...  # 做一些操作
#        # 退出时自动打印耗时
class Timer:
    pass  # <-- 完成类

# Q38 (3分) - Timer 上下文管理器 (@contextmanager 方式)
# 用 @contextmanager 装饰器重写 Q37 的 Timer:
#   进入 with 块时记录开始时间, 退出时打印耗时 (格式: "耗时: X.XXXXs")
# 用法: with q38_timer():
#           ...  # 做一些操作
#        # 退出时自动打印耗时
def q38_timer():
    pass  # <-- 完成上下文管理器函数


# =============================================================================
# 第 14 节：functools / itertools (8分)
# =============================================================================

# Q39 (4分) [MANUAL] - lru_cache / partial / reduce 的作用及示例
# 用注释写在这里即可.

# Q40 (4分) - itertools 函数示例
# (a) product([1,2], ["a","b"]) 笛卡尔积 -> 赋给 q40_a
# (b) permutations([1,2,3], 2) 排列 -> 赋给 q40_b
# (c) combinations([1,2,3], 2) 组合 -> 赋给 q40_c
# (d) groupby 示例用注释写 (不计分)
q40_a = None       # <-- 列表
q40_b = None  # <-- 列表
q40_c = None  # <-- 列表
# groupby 示例用注释写


# =============================================================================
# 第 15 节：继承与抽象 (6分)
# =============================================================================

# Q41 (3分) [MANUAL] - MRO 多继承: class C(A,B) 调用 who() 打印什么？
q41_output = None  # <-- 字符串

# Q42 (3分) - ABC 抽象基类: Animal + Dog
# Animal(ABC):
#   @abstractmethod make_sound(): 抽象方法
#   sleep(): 具体方法, print("Zzz...") 即可
# Dog(Animal):
#   make_sound(): 返回 "Woof!"
class Animal(ABC):
    pass  # <-- 完成抽象基类

class Dog(Animal):
    pass  # <-- 完成子类


# =============================================================================
# ==================== 自动判卷系统 (勿修改以下内容) ============================
# =============================================================================

class Grader:
    def __init__(self):
        self.total = 0
        self.earned = 0
        self.results = []

    def check(self, name, points, fn):
        self.total += points
        try:
            ok = fn()
            if ok:
                self.earned += points
                self.results.append(f"  [PASS] {name} (+{points})")
            else:
                self.results.append(f"  [FAIL] {name} (+0/{points})")
        except Exception as e:
            self.results.append(f"  [FAIL] {name} (+0/{points}) -- {e}")

    def manual(self, name, points):
        """概念题, 不计入自动评分但提示"""
        self.results.append(f"  [MANUAL] {name} -- 概念题, 需人工检查 (满分为{points}分)")

    def print_report(self):
        print("\n" + "=" * 60)
        print("  判 卷 结 果")
        print("=" * 60)
        for r in self.results:
            print(r)
        print("-" * 60)
        auto_total = self.total - sum(1 for r in self.results if "[MANUAL]" in r) * 0  # doesn't subtract
        auto_total = self.total  # manual already excluded
        print(f"  自动评分: {self.earned}/{auto_total}")
        print("  注: [MANUAL] 标记的概念题需人工对照检查, 不在此分数中")
        if self.earned >= self.total * 0.8:
            print("  *** 非常扎实！")
        elif self.earned >= self.total * 0.6:
            print("  *** 继续加油！")
        else:
            print("  *** 把学习材料再看一遍, 然后重做！")
        print("=" * 60)


if __name__ == "__main__":
    g = Grader()

    # ---- Q1 ----
    g.check("Q1 - 不可变类型列举", 2, lambda: set(x.lower() for x in q1_answer) >= {"int", "float", "str", "tuple", "bool", "frozenset", "bytes"} and len(q1_answer) >= 4)

    g.manual("Q2 - 小整数缓存 is 判断", 2)
    g.manual("Q3 - None 类型与布尔上下文", 2)

    # ---- Q4 ----
    def t4():
        return (q4_a == "Hello, World!"
                and q4_b == "  hello, world!  "
                and q4_c == "  HELLO, WORLD!  "
                and q4_d is not None and isinstance(q4_d, str))
    g.check("Q4 - 字符串基本操作", 2, t4)

    # ---- Q5 ----
    g.check("Q5 - f-string 格式化", 2, lambda: q5_result == "Alice is 25 years old, pi = 3.142")

    # ---- Q6 ----
    g.check("Q6 - join/split", 2, lambda: q6_a == "a,b,c" and q6_b == ["a", "b", "c"])

    # ---- Q7 ----
    g.check("Q7 - for-else 质数", 2, lambda: set(q7_primes) == {2,3,5,7,11,13,17,19} and len(q7_primes) == 8)

    # ---- Q8 ----
    def t8():
        names_q8 = ["Alice", "Bob", "Charlie"]
        scores_q8 = [85, 92, 78]
        expected_lines = []
        for i, (name, score) in enumerate(zip(names_q8, scores_q8)):
            nth = ["1st", "2nd", "3rd"][i]
            expected_lines.append(f"{nth}: {name} got {score}")
        return q8_enumerate_lines == expected_lines and q8_zip_lines == expected_lines
    g.check("Q8 - enumerate + zip", 2, t8)

    # ---- Q9 ----
    g.check("Q9 - range", 2, lambda: q9_range1 == list(range(10, 0, -1)) and q9_range2 == list(range(0, 10, 3)))

    # ---- Q10 ----
    def t10():
        import operator
        expected = {"+": 15, "-": 5, "*": 50, "/": 2}
        return isinstance(q10_dispatch, dict) and all(q10_dispatch.get(k) == v for k, v in expected.items())
    g.check("Q10 - dict dispatch", 2, t10)

    # ---- Q11 ----
    g.check("Q11 - 切片五连", 2, lambda: (
        q11_a == [0,1,2,3,4] and q11_b == [5,6,7,8,9]
        and q11_c == [2,4,6] and q11_d == [9,8,7,6,5,4,3,2,1,0]
        and q11_e == [0,2,4,6,8]
    ))

    # ---- Q12 ----
    g.check("Q12 - 切片原地插入", 2, lambda: q12_arr == [1, 2, 10, 20, 3, 4, 5])

    # ---- Q13 ----
    g.check("Q13 - 反转字符串", 2, lambda: q13_a == "olleh")

    # ---- Q14 ----
    g.check("Q14 - 推导式三连", 3, lambda: (
        q14_a == [x**2 for x in range(10)]
        and q14_b == [x for x in [x**2 for x in range(10)] if x % 2 == 0]
        and q14_c == {x: x**3 for x in range(5)}
    ))

    # ---- Q15 ----
    g.check("Q15 - 展平嵌套列表", 3, lambda: q15_flattened == [1,2,3,4,5,6,7,8,9])

    # ---- Q16 ----
    def t16():
        expected = [n for n in range(2, 51) if all(n % d != 0 for d in range(2, int(n**0.5)+1))]
        return q16_primes == expected
    g.check("Q16 - 一行质数推导", 4, t16)

    # ---- Q17 ----
    def t17():
        import io, sys
        buf = io.StringIO()
        old_stdout = sys.stdout
        sys.stdout = buf
        try:
            q17_print_all(1, 2, 3, name="Alice", age=25)
        finally:
            sys.stdout = old_stdout
        output = buf.getvalue()
        return "1" in output and "3" in output and "Alice" in output and "25" in output
    g.check("Q17 - *args **kwargs", 2, t17)

    # ---- Q18 ----
    def t18():
        # outer: 30, global: 10
        return q18_outer == 30 and q18_global == 10
    g.check("Q18 - nonlocal/global", 2, t18)

    # ---- Q19 ----
    def t19():
        r1 = q19_append_to_list("a")
        r2 = q19_append_to_list("b")
        r3 = q19_append_to_list("c")
        return r1 == ["a"] and r2 == ["b"] and r3 == ["c"]
    g.check("Q19 - 可变默认参数修正", 2, t19)

    # ---- Q20 ----
    def t20():
        try:
            sq_ok = q20_a(5) == 25
        except:
            sq_ok = False
        sorted_ok = q20_b == ["kiwi", "pear", "apple", "banana"]
        return sq_ok and sorted_ok
    g.check("Q20 - lambda", 2, t20)

    g.manual("Q21 - 内置函数解释", 2)

    # ---- Q22 ----
    def t22():
        nums = [1,2,3,4,5]
        return (q22_a == [1,4,9,16,25]
                and q22_b == [2,4]
                and q22_c == [x**2 for x in nums]
                and q22_d == [x for x in nums if x % 2 == 0])
    g.check("Q22 - map/filter + 列表推导", 2, t22)

    # ---- Q23 ----
    g.check("Q23 - sorted 按值排序", 2, lambda: q23_sorted_by_value == [("a", 3), ("c", 2),  ("b", 1)])

    g.manual("Q24 - set vs frozenset", 2)

    # ---- Q25 ----
    g.check("Q25 - set 判断异位词", 2, lambda: q25_a == True)

    # ---- Q26 ----
    def t26():
        expected = []
        seen = set()
        for x in [1,2,2,3,3,3,4,4,4,4]:
            if x not in seen:
                expected.append(x)
                seen.add(x)
        return q26_a == expected
    g.check("Q26 - 去重保序", 2, t26)

    # ---- Q27 ----
    def t27():
        @q27_log_call
        def add(a, b):
            return a + b
        import io, sys
        buf = io.StringIO()
        old = sys.stdout
        sys.stdout = buf
        try:
            result = add(3, 4)
        finally:
            sys.stdout = old
        output = buf.getvalue()
        return result == 7 and "add" in output and "3" in output
    g.check("Q27 - @log_call 装饰器", 3, t27)

    # ---- Q28 ----
    def t28():
        @q28_timeout(10)
        def fast():
            return "ok"
        result = fast()
        return result == "ok"
    g.check("Q28 - @timeout 装饰器", 3, t28)

    # ---- Q29 ----
    def t29():
        @CountCalls
        def say_hi():
            return "hi"
        say_hi()
        say_hi()
        return say_hi.count == 2
    g.check("Q29 - 类装饰器 CountCalls", 4, t29)

    # ---- Q30 ----
    def t30():
        c1 = list(q30_countdown(5)) == [5,4,3,2,1]
        c2 = list(q30_multiples_of_7) == [7,14,21,28,35,42,49,56,63,70,77,84,91,98]
        c3 = list(q30_my_chain([1,2], [3,4], [5,6])) == [1,2,3,4,5,6]
        return c1 and c2 and c3
    g.check("Q30 - 生成器三连", 4, t30)

    # ---- Q31 ----
    g.check("Q31 - 手写 RangeIterator", 4, lambda: list(RangeIterator(5)) == [0,1,2,3,4])

    # ---- Q32 ----
    def t32():
        acc = BankAccount("Alice", 100)
        acc.deposit(50)
        ok1 = acc.balance == 150
        acc.withdraw(30)
        ok2 = acc.balance == 120
        ok3 = acc.owner == "Alice"
        ok4 = str(acc) == "BankAccount(Alice, balance=120)"
        try:
            acc.withdraw(999)
            ok5 = False
        except ValueError:
            ok5 = True
        # check property: balance should not be directly settable
        try:
            acc.balance = 0
            ok6 = False
        except AttributeError:
            ok6 = True
        return ok1 and ok2 and ok3 and ok4 and ok5 and ok6
    g.check("Q32 - BankAccount 类", 4, t32)

    # ---- Q33 ----
    def t33():
        ok1 = DateUtils.from_iso("2024-12-25") == (2024, 12, 25)
        ok2 = DateUtils.is_leap_year(2024) == True
        ok3 = DateUtils.is_leap_year(2023) == False
        ok4 = DateUtils.is_leap_year(2000) == True
        ok5 = DateUtils.is_leap_year(1900) == False
        return ok1 and ok2 and ok3 and ok4 and ok5
    g.check("Q33 - DateUtils @classmethod/@staticmethod", 4, t33)

    # ---- Q34 ----
    def t34():
        d = StrReprDemo()
        r1 = repr(d)
        r2 = str(d)
        return isinstance(r1, str) and isinstance(r2, str) and r1 != r2
    g.check("Q34 - __str__ vs __repr__", 4, t34)

    # ---- Q35 ----
    def t35():
        pl = Playlist(["a", "b", "c"])
        ok1 = len(pl) == 3
        ok2 = pl[0] == "a"
        ok3 = ("b" in pl) == True
        pl[0] = "x"
        ok4 = pl[0] == "x"
        return ok1 and ok2 and ok3 and ok4
    g.check("Q35 - Playlist 魔术方法", 4, t35)

    # ---- Q36 ----
    g.check("Q36 - Multiplier __call__", 4, lambda: Multiplier(3)(5) == 15 and Multiplier(2)(100) == 200)

    # ---- Q37 ----
    def t37():
        import io, sys
        buf = io.StringIO()
        old = sys.stdout
        sys.stdout = buf
        try:
            with Timer():
                pass
        finally:
            sys.stdout = old
        return "s" in buf.getvalue().lower()  # should contain timing info
    g.check("Q37 - Timer 类方式", 3, t37)

    # ---- Q38 ----
    def t38():
        import io, sys
        buf = io.StringIO()
        old = sys.stdout
        sys.stdout = buf
        try:
            with q38_timer():
                pass
        finally:
            sys.stdout = old
        return "s" in buf.getvalue().lower()
    g.check("Q38 - Timer @contextmanager", 3, t38)

    g.manual("Q39 - functools 三件套", 4)

    # ---- Q40 ----
    def t40():
        ok1 = q40_a == list(product([1,2], ["a","b"]))
        ok2 = q40_b == list(permutations([1,2,3], 2))
        ok3 = q40_c == list(combinations([1,2,3], 2))
        return ok1 and ok2 and ok3
    g.check("Q40 - itertools 示例", 4, t40)

    # ---- Q41 ----
    g.check("Q41 - MRO 多继承", 3, lambda: q41_output == "A")

    # ---- Q42 ----
    def t42():
        dog = Dog()
        ok1 = dog.make_sound() == "Woof!"
        ok2 = isinstance(dog, Animal)
        # sleep should print or return without error
        dog.sleep()
        return ok1 and ok2
    g.check("Q42 - ABC 抽象基类", 3, t42)

    g.print_report()
