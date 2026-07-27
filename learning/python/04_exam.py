"""
Python 面试综合测试卷
======================
基于学习计划全部内容出题，覆盖所有面试高频考点。
每道题请手写实现，不要看答案。

考试规则：
  - 每个函数体内 pass 替换为你的实现
  - 注释里的「预期输出」供你自测
  - 边做边跑，通过输出验证答案
  - 重点关注面试高频板块：装饰器 / 生成器 / OOP / 拷贝 / 算法
"""

import enum
from functools import wraps, partial, reduce, lru_cache
from collections import deque, Counter, defaultdict, OrderedDict
from contextlib import contextmanager
from itertools import chain, permutations, combinations, product, groupby, islice, tee, zip_longest, count, cycle
from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import List, Dict, Optional, Any, Callable, TypeVar, Generic
import heapq
import bisect
import re
import copy
import time
import json
import os
import sys
import gc
import unittest
import logging
import math


# ============================================================
#  第一阶段：基础语法
# ============================================================

# ---------- 1. 数据类型 & 字符串 ----------

# 题1：用 f-string 格式化输出
# 输入：name="Alice", age=25, score=92.567
# 要求输出："姓名: Alice, 年龄: 25, 成绩: 92.57"
def exam_fstring(name: str, age: int, score: float) -> str:
    return f"姓名: {name}, 年龄: {age}, 成绩: {score:.2f}"
    pass


# 题2：字符串切片与反转
# 输入："hello world"
# 要求返回反转后的字符串，以及每两个字符取一个的结果（步长2）
def exam_slice_reverse(s: str) -> tuple:
    # 返回 (反转字符串, 步长2字符串)
    return s[::-1], s[::2]


# 题3：strip / split / join 组合
# 输入："  apple, banana , cherry , "
# 要求返回一个列表：['apple', 'banana', 'cherry']（去除空白、去逗号分隔）
def exam_string_clean(s: str) -> list:
    return [x.strip() for x in s.split(',') if x.strip()]
    pass


# ---------- 2. 控制流 ----------

# 题4：for-else 实现找质数
# 输入一个整数列表，返回其中第一个质数；如果没有质数，返回 -1
# 要求：必须用 for-else 实现
def exam_find_first_prime(nums: list) -> int:
    for i in nums:
        if i < 2:
            continue
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            return i
    return -1
    pass


# 题5：enumerate 和 zip 联合使用
# 输入两个等长列表 names 和 scores，返回 "序号. name: score" 的字符串列表
# 序号从 1 开始，只包含 score >= 60 的项
# 输入: names=["Alice","Bob","Charlie"], scores=[85,55,92]
# 预期: ["1. Alice: 85", "2. Charlie: 92"]
def exam_enumerate_zip(names: list, scores: list) -> list:
    # 原错误写法（序号 i+1 是位置而非及格项连续计数）
    # result = []
    # for i, name in enumerate(names):
    #     if i > len(scores):
    #         return result
    #     if scores[i] >= 60:
    #         result.append(f"{i+1}. {name}: {scores[i]}")
    # return result
    # 正解：
    result = []
    seq = 0
    for name, score in zip(names, scores):
        if score >= 60:
            seq += 1
            result.append(f"{seq}. {name}: {score}")
    return result
    pass


# ---------- 3. 列表 / 元组 / 字典 / 集合 ----------

# 题6：列表推导式展平嵌套列表
# 输入：[[1,2],[3,4],[5,6]]
# 要求用列表推导式展平 -> [1,2,3,4,5,6]
def exam_flatten(nested: list) -> list:
    return [l for i in nested for l in i]
    pass


# 题7：列表推导式 + 条件 — 找出所有能被3或5整除的数
# 输入：[1,2,3,4,5,6,7,8,9,10,15]
# 要求返回能被3或5整除的数的平方
def exam_divisible_squares(nums: list) -> list:
    return [n**2 for n in nums if n % 3 == 0 or n % 5 == 0]
    pass


# 题8：元组拆包交换两个变量（一行代码）
# 输入 a=3, b=5，原地交换
def exam_swap(a, b) -> tuple:
    # 返回交换后的 (a, b)
    return (b, a)
    pass


# 题9：字典 get 方法和 setdefault
# 实现一个函数，统计字符串中每个字符的索引列表
# 输入 "hello" -> {'h':[0], 'e':[1], 'l':[2,3], 'o':[4]}
# 要求：用 setdefault
def exam_char_index(s: str) -> dict:
    result = {}
    for i, c in enumerate(s):
        result.setdefault(c,[]).append(i)
    return result
    pass


# 题10：集合运算 — 找两个列表的交集和差集
# 输入: a=[1,2,3,4], b=[3,4,5,6]
# 返回: (交集, a-b差集, 对称差集)
def exam_set_ops(a: list, b: list) -> tuple:
    a1 = set(a)
    b1 = set(b)
    return (a1 & b1, a1 - b1, a1 ^ b1)
    pass


# 题11：用一行代码判断列表是否有重复元素
def exam_has_duplicate(nums: list) -> bool:
    # 原错误写法（逻辑反了：== 为 True 表示无重复）
    # return len(set(nums)) == len(nums)
    # 正解：
    return len(set(nums)) != len(nums)
    pass


# ---------- 4. 函数参数 ----------

# 题12：实现一个接受 *args 和 **kwargs 的函数
# 要求返回: {"sum": 所有位置参数的和, "keys": 所有关键字参数的键列表（排序后）}
def exam_args_kwargs(*args, **kwargs) -> dict:
    return {
        "sum": sum(args),
        "keys": sorted(kwargs)
    }
    pass


 
# 题13：默认参数的陷阱
# 请实现 add_item_correct(item, lst=None)
def add_item_correct(item, lst=None):
    # 原错误写法（lst is None 时 return lst 返回了 None）
    # if lst is None:
    #     return lst
    # lst.append(item)
    # return lst
    # 正解：
    if lst is None:
        lst = []
    lst.append(item)
    return lst


# 题14：多返回值本质
# 写一个函数返回三个值，然后证明它们的类型是元组
def exam_multi_return():
    # 原错误写法（返回了2个值而非3个，未体现多返回值本质）
    # result = (1, "hello", 3.14)
    # return result, type(result)
    # 正解：Python 逗号分隔的多个值会自动打包为元组
    return 1, "hello", 3.14  # 类型：tuple
    pass


# ---------- 5. lambda & 内置函数 ----------

# 题15：用 sorted 和 lambda 按字典 value 降序排列
# 输入 {"a":3, "b":1, "c":2} -> [("a",3), ("c",2), ("b",1)]
def exam_sort_dict_by_value(d: dict) -> list:
    # 原错误写法（lambda 过于复杂且缺少 reverse=True）
    # result = []
    # for i in d:
    #     result.append((i, d[i]))
    # result = sorted(result, key=lambda x: d[x[0]])
    # return result
    # 正解：
    return sorted(d.items(), key=lambda x: x[1], reverse=True)
    pass


# 题16：用 filter 和 lambda 过滤出字符串长度 >= 5 的单词
def exam_filter_long(words: list) -> list:
    return list(filter(lambda x: len(x) >= 5, words))
    pass


# 题17：用 map 和 lambda 把列表每个元素翻倍
def exam_map_double(nums: list) -> list:
    return list(map(lambda x: x*2, nums))
    pass


# 题18：any / all — 判断列表中是否所有元素都是正数，是否存在负数
# 返回: (全是正数?, 存在负数?)
def exam_any_all(nums: list) -> tuple:
    return all(map(lambda x: x > 0, nums)), any(map(lambda x: x < 0, nums))
    pass


# ---------- 6. 作用域 ----------

# 题19：global 和 nonlocal 的区别
# 请在注释中说明下面代码各输出什么，并解释为什么
# 
# 示例代码：
# x = 10
# def outer():
#     x = 20
#     def inner():
#         global x      # 声明使用全局变量 x
#         x = 30
#     inner()
#     print("outer x:", x)  # 输出？
# outer()
# print("global x:", x)      # 输出？
# 
# y = 10
# def outer2():
#     y = 20
#     def inner():
#         nonlocal y    # 声明使用外层函数的 y
#         y = 30
#     inner()
#     print("outer y:", y)   # 输出？
# outer2()
# print("global y:", y)       # 输出？

# 然后实现一个使用 nonlocal 的闭包计数器：make_counter() 每次调用返回递增的数字
def make_counter():
    pass


# ============================================================
#  第二阶段：进阶特性（面试最高频！）
# ============================================================

# ---------- 7. 闭包 ----------

# 题20：写一个闭包 make_multiplier(n)，返回一个函数，该函数接收 x 返回 x * n
def exam_make_multiplier(n: int):
    # 返回一个函数
    pass


# 题21：闭包变量绑定陷阱 — 下面代码输出什么？请在注释中回答并给出修复
# funcs = []
# for i in range(5):
#     funcs.append(lambda: i)
# print([f() for f in funcs])  # 输出?
# 修复：使每个 lambda 捕获当前 i 的值


# ---------- 8. 装饰器（⭐⭐⭐⭐⭐ 面试必考） ----------

# 题22：手写一个计时器装饰器 @timer，打印函数执行时间
# 要求用 functools.wraps 保留元信息
def exam_timer():
    """在下面实现 @timer 装饰器"""
    pass


# 题23：手写带参数的装饰器 @retry(n)，执行失败时重试 n 次
# 如果函数抛出异常，则重试，直到成功或次数用完
def exam_retry():
    """在下面实现 @retry(n) 装饰器"""
    pass


# 题24：手写类装饰器 @CountCalls，统计函数被调用次数
# 要求可以通过 func.call_count 访问调用次数
def exam_class_decorator():
    """在下面实现 @CountCalls 类装饰器"""
    pass


# 题25：实战 — 实现一个缓存装饰器 @memoize（类似 lru_cache 的简化版）
# 缓存函数调用结果，相同参数直接返回缓存值
def exam_memoize():
    """在下面实现 @memoize 装饰器"""
    pass


# ---------- 9. 生成器 & 迭代器 ----------

# 题26：用 yield 实现斐波那契数列生成器
# fib_gen(n) 生成前 n 个斐波那契数
def exam_fib_gen(n: int):
    pass


# 题27：生成器表达式 vs 列表推导式
# 注释回答：生成器表达式相比列表推导式的优势是什么？什么场景用哪个？
# 然后：用一个生成器表达式求 1~1000000 的平方和（不用列表推导式——占多少内存？）


# 题28：yield from 的用法
# 实现函数 flatten_gen(nested_list) 用 yield from 展平嵌套列表
# 输入 [[1,2], [3,4], [5]] -> 逐个 yield 1,2,3,4,5
def exam_yield_from(nested_list):
    pass


# 题29：自定义迭代器类
# 实现一个 RangeIterator(start, end, step)，支持 for 循环
class ExamRangeIterator:
    pass


# 题30：itertools 实战
# 用 itertools.combinations 列出列表中所有长度为2的组合
# 用 itertools.product 求两个列表的笛卡尔积
# 用 itertools.groupby 把 [1,1,2,2,3,3] 按值分组
def exam_itertools():
    """在注释中回答并手写实现"""
    pass


# ---------- 10. 面向对象 ----------

# 题31：实现一个 Vector2D 类
# 要求支持：v1 + v2（__add__）、str(v)（__str__）、v[0]/v[1]（__getitem__）
#         len(v)（__len__）、v1 == v2（__eq__）、abs(v)返回模长
class Vector2D:
    pass


# 题32：@property 的使用
# 实现一个 Temperature 类，内部存摄氏温度 _celsius
# 通过 @property 提供 celsius 和 fahrenheit 两个属性的读写
# fahrenheit 是一个计算属性（公式：F = C * 9/5 + 32）
class Temperature:
    pass


# 题33：@classmethod vs @staticmethod
# 实现 Person 类：
#   - __init__(name, birth_year)
#   - @classmethod from_birth_string(cls, s: str) 从 "张三,1990" 创建实例
#   - @staticmethod is_adult(age: int) -> bool 判断是否成年
class Person:
    pass


# 题34：继承与 super()
# 实现 Animal（基类，有 name 属性和 speak() 抽象方法）
# Dog 继承 Animal，speak() 返回 "Woof!"
# Cat 继承 Animal，speak() 返回 "Meow!"
# 所有子类的 __init__ 必须用 super() 调用父类
class Animal(ABC):
    pass


class Dog(Animal):
    pass


class Cat(Animal):
    pass


# 题35：鸭子类型 — 写一个函数 describe(obj)
# 如果 obj 有 __len__ 方法，打印其长度
# 如果 obj 有 __iter__ 方法（但不是 str），打印其所有元素
# 否则打印 "未知类型"
def exam_duck_typing(obj):
    pass


# ---------- 11. 上下文管理器 ----------

# 题36：用类实现上下文管理器 — 文件自动关闭
class ExamFileManager:
    # 实现 __enter__ 和 __exit__
    pass


# 题37：用 @contextmanager 实现计时器上下文管理器
# 用法：
#   with exam_timer_cm():
#       time.sleep(1)
# 自动打印耗时
@contextmanager
def exam_timer_cm():
    pass


# ---------- 12. 拷贝 & 对象模型 ----------

# 题38：浅拷贝 vs 深拷贝（⭐⭐⭐⭐ 面试必考）
# 给定嵌套列表 a = [[1,2], [3,4]]
# 请注释回答：
#   - b = a 是什么？修改 b[0][0] 会影响 a 吗？
#   - b = copy.copy(a)（浅拷贝）修改 b[0][0] 会影响 a 吗？
#   - b = copy.deepcopy(a)（深拷贝）修改 b[0][0] 会影响 a 吗？
#   - is vs == 的区别？
# 用代码验证你的回答
def exam_copy_demo():
    pass


# ---------- 13. 可变/不可变对象 ----------

# 题39：注释回答 — 下面代码输出什么？
# a = 256
# b = 256
# print(a is b)  # ?
# a = 257
# b = 257
# print(a is b)  # ?  (小整数缓存机制)
# 解释 Python 的 intern 机制


# 题40：函数参数传递 — 传的是对象的引用（call by sharing）
# 下面代码输出什么？为什么？
# def f(lst):
#     lst = lst + [4]  # 创建了新列表
# def g(lst):
#     lst += [4]       # 原地修改
# a = [1,2,3]; f(a); print(a)
# b = [1,2,3]; g(b); print(b)


# ============================================================
#  第三阶段：数据结构 & 算法
# ============================================================

# ---------- 14. collections 模块 ----------

# 题41：用 Counter 统计词频并输出 Top-3
# 输入文本字符串，返回出现频率最高的3个单词及其频率
def exam_top3_words(text: str) -> list:
    pass


# 题42：用 defaultdict 实现词频统计（不用 Counter，手动实现）
# 返回 {"word": count, ...}
def exam_word_count(text: str) -> dict:
    pass


# 题43：用 deque 实现固定大小的滑动窗口
# 输入列表和窗口大小 k，返回每个窗口的最大值（提示：单调队列）
# 输入: nums=[1,3,-1,-3,5,3,6,7], k=3
# 输出: [3,3,5,5,6,7]
def exam_sliding_window_max(nums: list, k: int) -> list:
    pass


# ---------- 15. heapq ----------

# 题44：用 heapq 实现优先级队列
# 每个任务 (priority, task_name)，priority 小的优先出队
class ExamPriorityQueue:
    pass


# 题45：用堆实现 Top-K 问题
# 从无序数组中找出第 K 大的元素（不用完全排序）
def exam_kth_largest(nums: list, k: int) -> int:
    pass


# 题46：合并 K 个有序列表
def exam_merge_k_sorted(lists: List[List[int]]) -> List[int]:
    pass


# ---------- 16. bisect ----------

# 题47：用 bisect 实现二分查找 — 在一个排序列表中插入元素并保持有序
def exam_insert_sorted(arr: list, x: int):
    pass


# 题48：用 bisect 找 target 在排序数组中的插入位置（左边界和右边界）
# 返回 (left_index, right_index)
def exam_bisect_range(arr: list, target: int) -> tuple:
    pass


# ---------- 17. 算法模板 ----------

# 题49：手写快速排序（原地版本）
def exam_quicksort(arr: list):
    pass


# 题50：二叉树中序遍历（迭代版本，用栈，不用递归）
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def exam_inorder_iterative(root: TreeNode) -> list:
    pass


# 题51：二叉树的最大深度（递归一行 + BFS 两种方式）
def exam_max_depth(root: TreeNode) -> int:
    pass


# 题52：图的 DFS 和 BFS
# 给定邻接表 graph = {node: [neighbors]}，写 DFS 和 BFS 遍历，返回遍历序列
def exam_graph_dfs(graph: dict, start) -> list:
    pass


def exam_graph_bfs(graph: dict, start) -> list:
    pass


# 题53：0-1 背包问题（一维 DP）
# weights, values, capacity -> 最大价值
def exam_knapsack(weights: list, values: list, capacity: int) -> int:
    pass


# 题54：最长公共子序列（LCS）
def exam_lcs(s1: str, s2: str) -> int:
    pass


# 题55：并查集
# 实现带路径压缩和按秩合并的 UnionFind
# 包含：find, union, connected 方法
class ExamUnionFind:
    pass


# 题56：字典树 Trie
# 实现 insert 和 search 和 starts_with
class ExamTrie:
    pass


# 题57：前缀和 — 区间求和 O(1)
# 给定数组，多次查询任意区间 [i, j] 的和
class ExamPrefixSum:
    # __init__ 构建前缀和数组
    # range_sum(i, j) 返回和
    pass


# ---------- 18. 排序 ----------

# 题58：多级排序
# 给定学生列表 [(name, grade, score)]，先按 grade 升序，再按 score 降序
def exam_multilevel_sort(students: list) -> list:
    pass


# 题59：自定义排序 — 按字符串长度排序，同长按字母序
def exam_sort_by_length(words: list) -> list:
    pass


# ---------- 19. 正则表达式 ----------

# 题60：提取字符串中所有邮箱地址
def exam_extract_emails(text: str) -> list:
    pass


# 题61：验证手机号格式（中国手机号：1[3-9]\d{9}）
def exam_is_valid_phone(s: str) -> bool:
    pass


# 题62：用 re.sub 把敏感词替换为 ***
# 输入: text="你好，请联系admin或者root。"，敏感词=["admin", "root"]
# 输出: "你好，请联系***或者***。"
def exam_censor(text: str, keywords: list) -> str:
    pass


# ---------- 20. 字符串 ----------

# 题63：解释字符串比大小的原理（注释回答）
# "10" < "2" 为什么是 True？
# 如何实现自然排序（"2" 排在 "10" 前面）？


# ============================================================
#  第四阶段：高级特性
# ============================================================

# ---------- 21. 并发 & GIL ----------

# 题64：注释回答 — GIL 是什么？影响什么类型的程序？如何绕过？
def exam_gil_explain():
    """在注释中回答"""
    pass


# 题65：用 concurrent.futures.ThreadPoolExecutor 并发下载多个 URL
# 模拟：每个 URL 返回 f"content of {url}"（用 time.sleep 模拟延迟）
def exam_thread_pool(urls: list) -> list:
    pass


# ---------- 22. 元编程 ----------

# 题66：用 type() 动态创建一个类
# 等价于 class Person: name = "anonymous"
def exam_type_create():
    pass


# 题67：__slots__ 的作用
# 注释回答：__slots__ 解决了什么问题？它的原理是什么？有什么限制？
# 实现一个带 __slots__ 的 Point 类
class ExamSlottedPoint:
    __slots__ = ('x', 'y')
    pass


# 题68：getattr / setattr / hasattr 反射
# 实现一个函数 set_attrs(obj, **kwargs)，用反射动态给对象设置属性
def exam_set_attrs(obj, **kwargs):
    pass


# ---------- 23. 常用内置库 ----------

# 题69：json 序列化和反序列化
# 把一个 Python dict 序列化为 JSON 字符串，再反序列化回来
def exam_json_roundtrip(d: dict) -> dict:
    pass


# 题70：dataclass 的用法
# 用 @dataclass 定义一个 Point3D 类，有 x, y, z 三个字段，默认都是0
# 并打印两个实例的比较结果
@dataclass
class ExamPoint3D:
    pass


# 题71：typing 类型注解
# 给下面的函数加上完整的类型注解
def exam_typing_demo(data, key, default):
    """
    data: 字典
    key: 要查找的键
    default: 默认值
    返回: 值或默认值
    """
    return data.get(key, default)


# 题72：os / sys 基础
# 写一个函数，返回当前工作目录、Python 版本、命令行参数列表
def exam_os_sys() -> dict:
    pass


# ---------- 24. 内存管理与性能 ----------

# 题73：注释回答 — Python 的垃圾回收机制
# 引用计数是什么？循环引用怎么解决？（gc 模块）


# 题74：字符串拼接性能
# 注释回答：为什么大量拼接时 join() 比 += 快得多？
# 写代码用 timeit 对比两种方式的性能


# 题75：列表 vs 生成器的内存对比
# 生成 range(10000000) 的列表和生成器，各占多少内存？（用 sys.getsizeof）
def exam_memory_compare():
    pass


# ---------- 25. 测试与调试 ----------

# 题76：写一个简单的 unittest 测试用例
# 测试函数 add(a, b) 的 3 种情况：正数、负数、零
class ExamTestAdd(unittest.TestCase):
    pass


# 题77：assert 断言的用法
# 写一个函数 divide(a, b)，用 assert 确保 b != 0
def exam_safe_divide(a, b):
    pass


# 题78：logging 基本用法
# 配置 logging 输出到控制台，格式包含时间、级别、消息
# 分别输出 DEBUG、INFO、WARNING、ERROR 级别的日志
def exam_logging_demo():
    pass


# ---------- 26. 编码规范 ----------

# 题79：PEP 8 常见规范（注释回答）
# 函数名、变量名用什么风格？类名用什么风格？常量用什么风格？
# import 的顺序是什么？每行最大字符数是多少？
def exam_pep8():
    pass


# 题80：写一个 docstring 规范的三引号文档字符串
# 给下面的函数写一个完整的 docstring（包含参数、返回值、示例）
def add(a: int, b: int) -> int:
    pass


# ============================================================
#  第五阶段：实战应用
# ============================================================

# ---------- 27. 数据处理 ----------

# 题81：用列表推导式 + lambda 模拟 numpy 的向量化操作
# 两个等长列表 a, b，返回 a+b, a-b, a*b 的元素级运算结果
def exam_vector_ops(a: list, b: list) -> tuple:
    # 返回 (相加列表, 相减列表, 相乘列表)
    pass


# 题82：用 csv 模块读/写（用 StringIO 模拟）
# 把 [{"name":"Alice","age":25},{"name":"Bob","age":30}] 写成 CSV 格式字符串
def exam_csv_write(data: list) -> str:
    pass


# ---------- 28. 命令行工具 ----------

# 题83：用 argparse 设计一个 CLI
# 注释写出：如何用 argparse 实现一个接受 --input, --output, --verbose 参数的命令行程序？
def exam_argparse_design():
    """在注释中写出完整的 argparse 使用代码"""
    pass


# ---------- 29. 综合实战 ----------

# 题84：手写 LRU Cache（⭐⭐⭐ LeetCode 146）
# 用 OrderedDict 实现，要求 O(1) get 和 put
class ExamLRUCache:
    # __init__(self, capacity)
    # get(self, key) -> int  (不存在返回-1)
    # put(self, key, value)
    pass


# 题85：手写单例模式（两种方式）
# 方式1：用 __new__ 实现
# 方式2：用装饰器实现
class ExamSingletonNew:
    _instance = None

    def __new__(cls, *args, **kwargs):
        pass


def exam_singleton_decorator():
    """在下面实现单例装饰器"""
    pass


# ============================================================
# 题86-90：综合陷阱题
# ============================================================

# 题86：下面代码输出什么？为什么？
# a = (1, 2, [3, 4])
# a[2].append(5)
# print(a)
# 元组中的可变对象可以修改吗？为什么？

# 题87：下面代码输出什么？
# def f(a=[]):
#     a.append(1)
#     return a
# print(f(), f(), f())

# 题88：下面两个赋值有什么区别？
# a = [[]] * 5
# b = [[] for _ in range(5)]
# a[0].append(1) vs b[0].append(1)
# 输出 a 和 b 各是什么？

# 题89：Python 的 is 和 == 的区别？在什么场景下 a is b 为 True 但 a == b 也为 True？
# (考察 intern 机制、小整数缓存、字符串驻留)

# 题90：装饰器的执行顺序
# @decorator_a
# @decorator_b
# def foo(): pass
# 等价于什么？执行顺序是从上到下还是从下到上？


# ============================================================
# 测试入口：学生做完全部试题后运行
# ============================================================
if __name__ == "__main__":
    print("=" * 60)
    print("Python 面试综合测试卷")
    print("请逐个实现上面所有题目，然后运行本脚本自测")
    print("=" * 60)

    # --- 题1 ---
    assert exam_fstring(
        "Alice", 25, 92.567) == "姓名: Alice, 年龄: 25, 成绩: 92.57", "题1 失败"

    # --- 题2 ---
    rev, step2 = exam_slice_reverse("hello world")
    assert rev == "dlrow olleh", f"题2 反转失败: {rev}"
    assert step2 == "hlowrd", f"题2 步长失败: {step2}"

    # --- 题3 ---
    assert exam_string_clean("  apple, banana , cherry , ") == [
        "apple", "banana", "cherry"], "题3 失败"

    # --- 题4 ---
    assert exam_find_first_prime([4, 6, 8, 9]) == -1, "题4 无质数情况失败"
    assert exam_find_first_prime([4, 6, 7, 9]) == 7, "题4 找到质数情况失败"

    # --- 题5 ---
    assert exam_enumerate_zip(["Alice", "Bob", "Charlie"], [85, 55, 92]) == [
        "1. Alice: 85", "2. Charlie: 92"], "题5 失败"

    # --- 题6 ---
    assert exam_flatten([[1, 2], [3, 4], [5, 6]]) == [
        1, 2, 3, 4, 5, 6], "题6 失败"

    # --- 题7 ---
    assert exam_divisible_squares([1, 2, 3, 4, 5]) == [
        9, 25], f"题7 失败: {exam_divisible_squares([1, 2, 3, 4, 5])}"

    # --- 题8 ---
    assert exam_swap(3, 5) == (5, 3), "题8 失败"

    # --- 题9 ---
    assert exam_char_index("hello") == {'h': [0], 'e': [
        1], 'l': [2, 3], 'o': [4]}, "题9 失败"

    # --- 题10 ---
    inter, diff, sym = exam_set_ops([1, 2, 3, 4], [3, 4, 5, 6])
    assert inter == {3, 4}, f"题10 交集失败: {inter}"
    assert diff == {1, 2}, f"题10 差集失败: {diff}"
    assert sym == {1, 2, 5, 6}, f"题10 对称差集失败: {sym}"

    # --- 题11 ---
    assert exam_has_duplicate([1, 2, 3, 1]) == True, "题11 True 失败"
    assert exam_has_duplicate([1, 2, 3]) == False, "题11 False 失败"

    # --- 题12 ---
    r = exam_args_kwargs(1, 2, 3, name="Alice", age=25)
    assert r["sum"] == 6, f"题12 sum 失败: {r['sum']}"
    assert r["keys"] == ["age", "name"], f"题12 keys 失败: {r['keys']}"

    # --- 题81 ---
    add_r, sub_r, mul_r = exam_vector_ops([1, 2, 3], [4, 5, 6])
    assert add_r == [5, 7, 9], f"题81 相加失败: {add_r}"
    assert sub_r == [-3, -3, -3], f"题81 相减失败: {sub_r}"
    assert mul_r == [4, 10, 18], f"题81 相乘失败: {mul_r}"

    print("\n🎯 所有基础断言通过！继续完成剩余的算法和 OOP 题目。")
