"""
=============================================================================
Python 面试笔试 - 综合能力测试卷
=============================================================================
考试说明:
  - 本试卷共 6 大题, 满分 100 分
  - 请在每道题的注释下方编写你的答案代码
  - 题目涵盖：基础语法、高级特性、数据结构算法、面向对象、并发、陷阱题
  - 鼓励写出 Pythonic 的代码, 必要时可使用注释辅助说明思路
  - 写完直接 python 运行本文件即可自动判卷评分
=============================================================================
"""

import re
from collections import deque, Counter, defaultdict
from functools import wraps, lru_cache
from typing import List, Dict, Optional, Tuple
import heapq
import copy
import time
import math


# =============================================================================
# 第一部分：基础语法与数据结构 (20分, 每题5分)
# =============================================================================

# --- 第 1 题 (5分) ---
# 请用一行代码（列表推导式）生成一个列表, 包含 1 到 100 之间所有能被 3 整除但不能被 5 整除的数,
# 并将结果赋给变量 result_1。

# 你的答案:
result_1 = [x for x in range(1,101) if x%3==0 and x%5!=0]  # <-- 替换这一行为你的一行代码


# --- 第 2 题 (5分) ---
# 给定一个字符串 s = "hello world python", 请写代码统计每个字符出现的次数,
# 使用 collections.Counter 完成, 并将出现频率最高的前 3 个字符及其频次打印出来。
# 结果赋给变量 result_2。

# 你的答案:
from collections import Counter
s = "hello world python"
counter = Counter(s)
result_2 = counter.most_common(3)
for char,count in result_2:
  print(f"{char}: {count}")


# --- 第 3 题 (5分) ---
# 有两个列表 a = [1, 2, 3, 4, 5] 和 b = [3, 4, 5, 6, 7]。
# 请使用集合 (set) 操作, 分别求出交集、并集、差集 (a有b没有)。
# 将交集赋给 result_3_inter, 并集赋给 result_3_union, 差集赋给 result_3_diff。
# (注意: 集合是无序的, 评分时会转为 set 比较)

# 你的答案:
a = [1, 2, 3, 4, 5]
b = [3, 4, 5, 6, 7]
a1 = set(a)
b1 = set(b)
result_3_inter = a1.intersection(b1)   # <-- 交集
result_3_inter = a1 & b1   # <-- 交集
result_3_union = a1.union(b1)   # <-- 并集
result_3_union = a1 | b1   # <-- 并集
result_3_diff = a1.difference(b1)    # <-- a有b没有
result_3_diff = a1 - b1    # <-- a有b没有


# --- 第 4 题 (5分) ---
# 以下函数有 bug（可变默认参数陷阱）, 请指出问题, 并在下方写出修正后的版本。
#
# def add_item(item, items=[]):
#     items.append(item)
#     return items
# 后续执行时，如果没传items，每次都会默认在一个items里新增

# 你的答案（修正后的函数）:
def add_item(item, items=None):
  if items is None:
    return [item]
  else:
    items.append(item)
    return items


# =============================================================================
# 第二部分：高级特性 - 装饰器与生成器 (20分, 每题10分)
# =============================================================================

# --- 第 5 题 (10分) ---
# 请实现一个装饰器 @retry(max_attempts=3), 当被装饰的函数抛出异常时自动重试,
# 最多重试 max_attempts 次。如果所有重试都失败, 抛出最后一次的异常。
# 要求使用 functools.wraps 保留原函数的元信息。

# 你的答案:
from functools import wraps
def retry(max_attempts=3):
  def decorator(func):
    @wraps(func)
    def wrappers(*args, **kwargs):
      for i in range(max_attempts):
        try:
          result = func(*args, **kwargs)
          return result
        except Exception as e:
          if i == max_attempts-1:
            raise
    return wrappers
  return decorator



# --- 第 6 题 (10分) ---
# 请实现一个生成器函数 fibonacci(n), 用于生成前 n 个斐波那契数。
# 要求使用 yield 关键字, 不要一次性生成整个列表返回。
#
# 示例:
#   list(fibonacci(6)) -> [0, 1, 1, 2, 3, 5]

# 你的答案:
def fibonacci(n):
  a, b = 0, 1
  for _ in range(n):
    yield a
    a,b = b,a+b



# =============================================================================
# 第三部分：数据结构与算法 (30分, 每题10分)
# =============================================================================

# --- 第 7 题 (10分) ---
# 实现一个函数 top_k_frequent(nums, k), 返回数组中出现频率最高的 k 个元素。
# 要求时间复杂度不超过 O(n log k)。
#
# 示例:
#   top_k_frequent([1,1,1,2,2,3], 2) -> [1, 2]

# 你的答案:
def top_k_frequent(nums, k):
    pass  # <-- 请完成这个函数


# --- 第 8 题 (10分) ---
# 实现一个函数 is_valid_parentheses(s), 判断给定的字符串中的括号是否有效。
# 支持的括号类型: (), [], {}

# 示例:
#   is_valid_parentheses("()[]{}") -> True
#   is_valid_parentheses("([)]")   -> False
#   is_valid_parentheses("{[]}")   -> True

# 你的答案:
def is_valid_parentheses(s):
    pass  # <-- 请完成这个函数


# --- 第 9 题 (10分) ---
# 给定一个非负整数 numRows, 生成杨辉三角的前 numRows 行。

# 你的答案:
def generate_pascal_triangle(numRows):
    pass  # <-- 请完成这个函数


# =============================================================================
# 第四部分：面向对象编程 (10分)
# =============================================================================

# --- 第 10 题 (10分) ---
# 实现一个类 Vector2D, 满足以下要求:
#   1. 构造函数接受 x, y 两个坐标
#   2. 实现 __repr__ 方法, 返回 f"Vector2D({x}, {y})"
#   3. 实现 __add__ 方法, 支持两个 Vector2D 相加
#   4. 实现 @property 方法 magnitude, 返回向量的模长: sqrt(x^2 + y^2)
#   5. 实现 __eq__ 方法, 判断两个向量是否相等

# 你的答案:
class Vector2D:
    pass  # <-- 请完成这个类


# =============================================================================
# 第五部分：Python 陷阱与底层理解 (10分, 每题5分)
# =============================================================================

# --- 第 11 题 (5分) ---
# 阅读以下代码, 回答输出分别是什么？为什么？
#   a = [1, 2, 3]; b = a; c = a[:]
#   print(a == b)  # ?
#   print(a is b)  # ?
#   print(a == c)  # ?
#   print(a is c)  # ?
# 将你的答案写在下面 (每个问题的预期布尔值)

# 你的答案:
answer_11 = (None, None, None, None)  # <-- 替换为 (ans1, ans2, ans3, ans4)


# --- 第 12 题 (5分) ---
# 以下代码的输出是什么？请解释闭包延迟绑定的问题。
#   funcs = [lambda x: i * x for i in range(3)]
#   print([f(2) for f in funcs])
# 将预期输出写在下面:

# 你的答案:
answer_12 = None  # <-- 替换为预期的列表, 如 [0, 2, 4] 或 [4, 4, 4] 等


# =============================================================================
# 第六部分：并发与异步 (10分)
# =============================================================================

# --- 第 13 题 (10分) ---
# 以下是一段多线程代码, count 的最终值大概率不是 300000。请修改 increment 相关代码,
# 使用 threading.Lock 保证线程安全, 使得最终值精确等于 300000。
# 把修正后的 Counter 类和 increment 函数写在下方。

import threading

# 你的答案 (修正后):
class SafeCounter:
    pass  # <-- 请完成这个类, 保证线程安全

def safe_increment(counter):
    pass  # <-- 请完成这个函数, 每个线程调 100000 次


# =============================================================================
# ==================== 自动判卷系统 (勿修改以下内容) ============================
# =============================================================================

class Grader:
    def __init__(self):
        self.total = 0
        self.earned = 0
        self.results = []

    def check(self, name, points, fn):
        """fn 无异常返回 points 分, 异常返回 0 分"""
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

    def print_report(self):
        print("\n" + "=" * 60)
        print("  判 卷 结 果")
        print("=" * 60)
        for r in self.results:
            print(r)
        print("-" * 60)
        print(f"  总分: {self.earned}/{self.total}")
        if self.earned == self.total:
            print("  *** 满分！干得漂亮！")
        elif self.earned >= self.total * 0.8:
            print("  *** 很不错, 再接再厉！")
        elif self.earned >= self.total * 0.6:
            print("  *** 还有提升空间, 加油！")
        else:
            print("  *** 革命尚未成功, 继续刷题！")
        print("=" * 60)


if __name__ == "__main__":
    g = Grader()

    # --- 第 1 题 ---
    def t1():
        expected = [x for x in range(1, 101) if x % 3 == 0 and x % 5 != 0]
        return result_1 == expected
    g.check("Q1 - 列表推导式筛数", 5, t1)

    # --- 第 2 题 ---
    def t2():
        c = Counter("hello world python")
        expected = c.most_common(3)
        return result_2 == expected
    g.check("Q2 - Counter 最高频", 5, t2)

    # --- 第 3 题 ---
    def t3():
        a = [1, 2, 3, 4, 5]
        b = [3, 4, 5, 6, 7]
        return (
            set(result_3_inter) == set(a) & set(b)
            and set(result_3_union) == set(a) | set(b)
            and set(result_3_diff) == set(a) - set(b)
        )
    g.check("Q3 - 集合操作", 5, t3)

    # --- 第 4 题 ---
    def t4():
        r1 = add_item("a")
        r2 = add_item("b")
        r3 = add_item("c")
        return r1 == ["a"] and r2 == ["b"] and r3 == ["c"]
    g.check("Q4 - 可变默认参数修正", 5, t4)

    # --- 第 5 题 ---
    def t5():
        call_count = [0]

        @retry(max_attempts=3)
        def flaky():
            call_count[0] += 1
            if call_count[0] < 3:
                raise ValueError("fail")
            return "ok"

        result = flaky()
        return result == "ok" and call_count[0] == 3
    g.check("Q5 - retry 装饰器", 10, t5)

    # --- 第 6 题 ---
    def t6():
        return list(fibonacci(6)) == [0, 1, 1, 2, 3, 5] and list(fibonacci(1)) == [0]
    g.check("Q6 - fibonacci 生成器", 10, t6)

    # --- 第 7 题 ---
    def t7():
        r = top_k_frequent([1, 1, 1, 2, 2, 3], 2)
        return set(r) == {1, 2}
    g.check("Q7 - Top K 高频元素", 10, t7)

    # --- 第 8 题 ---
    def t8():
        return (
            is_valid_parentheses("()[]{}") == True
            and is_valid_parentheses("([)]") == False
            and is_valid_parentheses("{[]}") == True
            and is_valid_parentheses("") == True
            and is_valid_parentheses("(") == False
        )
    g.check("Q8 - 有效括号", 10, t8)

    # --- 第 9 题 ---
    def t9():
        r = generate_pascal_triangle(5)
        expected = [
            [1],
            [1, 1],
            [1, 2, 1],
            [1, 3, 3, 1],
            [1, 4, 6, 4, 1],
        ]
        return r == expected
    g.check("Q9 - 杨辉三角", 10, t9)

    # --- 第 10 题 ---
    def t10():
        v1 = Vector2D(3, 4)
        v2 = Vector2D(1, 2)
        v3 = v1 + v2

        c1 = repr(v1) == "Vector2D(3, 4)"
        c2 = v3 == Vector2D(4, 6)
        c3 = abs(v1.magnitude - 5.0) < 0.001
        c4 = Vector2D(1, 2) == Vector2D(1, 2)
        c5 = Vector2D(1, 2) != Vector2D(2, 1)
        return c1 and c2 and c3 and c4 and c5
    g.check("Q10 - Vector2D 类", 10, t10)

    # --- 第 11 题 ---
    def t11():
        a = [1, 2, 3]; b = a; c = a[:]
        expected = (a == b, a is b, a == c, a is c)
        return answer_11 == expected
    g.check("Q11 - is vs ==", 5, t11)

    # --- 第 12 题 ---
    def t12():
        return answer_12 == [4, 4, 4]
    g.check("Q12 - 闭包延迟绑定", 5, t12)

    # --- 第 13 题 ---
    def t13():
        counter = SafeCounter()
        threads = [threading.Thread(target=safe_increment, args=(counter,)) for _ in range(3)]
        for t in threads:
            t.start()
        for t in threads:
            t.join()
        # 检查 counter 是否有 .value 属性且等于 300000
        if hasattr(counter, 'value'):
            return counter.value == 300000
        elif hasattr(counter, 'get_value'):
            return counter.get_value() == 300000
        else:
            raise Exception("SafeCounter 需要有 .value 属性或 .get_value() 方法")
    g.check("Q13 - 线程安全计数", 10, t13)

    g.print_report()
