# Python 从入门到精通 — 面试备战学习计划

> 面向对象：已有 C++ 算法基础的面试准备者
> 核心目标：从零基础到能熟练运用 Python 解决面试中的各类问题

---

## 第一阶段：基础语法速通（利用 C++ 基础加速学习）

### 1.1 环境与基础
- [ ] Python 解释器与虚拟环境（venv / conda）
- [ ] 基础数据类型：`int`, `float`, `bool`, `str`, `None`
- [ ] 变量与动态类型 —— 与 C++ 静态类型的对比
- [ ] 输入输出：`input()`, `print()`, f-string 格式化

### 1.2 控制流
- [ ] `if / elif / else`（Python 没有 switch，注意缩进）
- [ ] `while` 循环
- [ ] `for ... in` 迭代（对比 C++ for 循环）
- [ ] `range()`, `enumerate()`, `zip()`
- [ ] `break`, `continue`, `else` 子句（`for-else` 是 Python 特色）

### 1.3 核心数据结构
- [ ] **列表 list**：增删改查、切片（`list[::-1]` 反转）、列表推导式
- [ ] **元组 tuple**：不可变序列、拆包
- [ ] **字典 dict**：哈希表、`get()`, `setdefault()`, `defaultdict`
- [ ] **集合 set**：去重、交并差运算、`frozenset`
- [ ] **字符串 str**：常用方法（`split/join/strip/replace/find`）

### 1.4 函数
- [ ] 定义与调用 `def`
- [ ] 位置参数、默认参数、关键字参数、`*args` / `**kwargs`
- [ ] 返回值与多返回值（本质是元组拆包）
- [ ] 作用域与 `global` / `nonlocal`

### 1.5 常用内置函数
- [ ] `len()`, `range()`, `enumerate()`, `zip()`, `map()`, `filter()`, `sorted()`, `reversed()`
- [ ] `any()`, `all()`, `sum()`, `max()`, `min()`
- [ ] `isinstance()`, `type()`, `id()`
- [ ] `lambda` 匿名函数

> **面试重点**：列表推导式、字典推导式、lambda、切片操作

---

## 第二阶段：进阶特性（面试高频考点）

### 2.1 函数式编程与高级函数
- [ ] `map / filter / reduce`（`reduce` 来自 `functools`）
- [ ] 列表推导式 vs `map/filter` 性能对比
- [ ] 生成器表达式（惰性求值）：`(x for x in range(10))`
- [ ] 闭包与装饰器（**面试必考**）
  - 装饰器原理：`@decorator` 等价于 `func = decorator(func)`
  - 带参数的装饰器
  - `functools.wraps` 保留原函数元信息
  - 类装饰器

### 2.2 迭代器与生成器
- [ ] 可迭代对象 vs 迭代器（`__iter__`, `__next__`）
- [ ] `yield` 与生成器函数
- [ ] `yield from`
- [ ] `itertools` 模块：`chain`, `product`, `permutations`, `combinations`, `groupby`

### 2.3 面向对象编程
- [ ] 类定义与 `__init__`
- [ ] 实例方法、类方法 `@classmethod`、静态方法 `@staticmethod`
- [ ] 属性装饰器 `@property`、`@setter`、`@deleter`
- [ ] 魔术方法（`__str__`, `__repr__`, `__len__`, `__getitem__`, `__call__`, `__enter__/__exit__`）
- [ ] 继承与 `super()`
- [ ] 抽象基类 `ABC` 与 `@abstractmethod`
- [ ] 鸭子类型与协议（`__len__` 使对象支持 `len()`）

### 2.4 上下文管理器
- [ ] `with` 语句
- [ ] 实现上下文管理器：`__enter__` / `__exit__`
- [ ] `contextlib.contextmanager` 装饰器方式

---

## 第三阶段：进阶数据操作与面试算法

### 3.1 常用数据结构操作（笔试高频）
- [ ] 列表作为栈、队列（`collections.deque`）
- [ ] `collections.Counter` — 频率统计
- [ ] `collections.defaultdict` — 默认值字典
- [ ] `collections.OrderedDict` — 有序字典
- [ ] `collections.heapq` — 堆（优先队列）
- [ ] `bisect` — 二分查找
- [ ] 排序：`list.sort()` vs `sorted()`、自定义 key

### 3.2 Python 实现算法模板（对比 C++）
- [ ] 快速排序、归并排序（Python 实现）
- [ ] 二叉树遍历（递归 vs 迭代）
- [ ] 图的 DFS / BFS
- [ ] 动态规划（备忘录 vs 自底向上）
- [ ] 并查集 Union-Find
- [ ] 字典树 Trie
- [ ] 前缀和与差分

### 3.3 字符串处理
- [ ] 正则表达式 `re` 模块（`search`, `match`, `findall`, `sub`, `split`）
- [ ] 字符串比大小的底层原理

---

## 第四阶段：高级特性与精通之路

### 4.1 并发与异步
- [ ] `threading` 与 `multiprocessing` 基础
- [ ] GIL 锁的含义与影响
- [ ] `concurrent.futures`（`ThreadPoolExecutor`, `ProcessPoolExecutor`）
- [ ] `asyncio` 异步编程：`async / await`、事件循环、`asyncio.gather`

### 4.2 元编程
- [ ] `type` 动态创建类
- [ ] 元类 `__metaclass__`
- [ ] `__slots__` 优化内存
- [ ] 描述符协议（`__get__`, `__set__`, `__delete__`）
- [ ] `getattr / setattr / hasattr` 反射

### 4.3 内建库深度掌握
- [ ] `functools`: `lru_cache`, `partial`, `reduce`, `wraps`
- [ ] `itertools`: `chain`, `islice`, `tee`, `zip_longest`, `count`, `cycle`
- [ ] `os` / `sys` / `shutil`
- [ ] `json` / `pickle` / `csv`
- [ ] `datetime` / `time`
- [ ] `typing`: `List`, `Dict`, `Optional`, `Any`, `Callable`, `TypeVar`, `Generic`
- [ ] `dataclasses.dataclass` — 数据类

### 4.4 内存管理与性能优化
- [ ] 引用计数与垃圾回收（`gc` 模块）
- [ ] 浅拷贝 vs 深拷贝（`copy.copy` vs `copy.deepcopy`）
- [ ] Python 对象模型（一切皆对象）
- [ ] 性能分析：`timeit`, `cProfile`, `line_profiler`
- [ ] 列表 vs 生成器的内存差异
- [ ] `__slots__` 节省内存
- [ ] 字符串拼接性能（`join` vs `+=`）

### 4.5 测试与调试
- [ ] `unittest` / `pytest` 测试框架
- [ ] `pdb` 调试器
- [ ] `logging` 日志模块
- [ ] `assert` 断言

### 4.6 编码规范与最佳实践
- [ ] PEP 8 编码规范
- [ ] PEP 20（Python之禅）
- [ ] 类型注解（type hints）
- [ ] 文档字符串（docstring）
- [ ] 模块与包组织

---

## 第五阶段：实战应用与开源

### 5.1 Web 开发（了解即可）
- [ ] Flask / FastAPI 基础
- [ ] RESTful API 设计

### 5.2 数据处理
- [ ] `numpy` 基础
- [ ] `pandas` 基础操作
- [ ] 数据可视化 `matplotlib`

### 5.3 Python 进阶项目实践
- [ ] 爬虫（`requests` + `BeautifulSoup` / `Scrapy`）
- [ ] 命令行工具（`argparse` / `click` / `typer`）
- [ ] 阅读并理解一个知名开源库的源码（如 `requests`, `flask`, `click`）

---

## 面试专项练习

### Python 面试高频考点（按重要性排序）

| 考点 | 重要性 | 说明 |
|------|--------|------|
| 装饰器 | ⭐⭐⭐⭐⭐ | 原理、实现、带参装饰器、`functools.wraps` |
| 列表推导式 | ⭐⭐⭐⭐⭐ | 与 for 循环对比、嵌套推导式 |
| 生成器与迭代器 | ⭐⭐⭐⭐⭐ | `yield`、生成器表达式、内存优势 |
| `*args` / `**kwargs` | ⭐⭐⭐⭐ | 可变参数、拆包 |
| 浅拷贝 vs 深拷贝 | ⭐⭐⭐⭐ | `is` vs `==`、可变/不可变对象 |
| GIL | ⭐⭐⭐⭐ | 含义、影响、如何绕过 |
| 上下文管理器 | ⭐⭐⭐⭐ | `with` 语句、自定义 |
| 魔术方法 | ⭐⭐⭐⭐ | 常见魔术方法 |
| 闭包 | ⭐⭐⭐⭐ | 变量捕获、nonlocal |
| `is` vs `==` | ⭐⭐⭐⭐ | 身份 vs 相等 |
| 元类 | ⭐⭐⭐ | 了解即可 |
| 异步编程 | ⭐⭐⭐ | `async/await` 基础 |

### 面试代码题示例
1. 实现一个带缓存的装饰器（类似 `lru_cache`）
2. 用生成器实现斐波那契数列
3. 手写单例模式（多种方式）
4. 实现一个上下文管理器（计时器、文件锁）
5. 用列表推导式简化嵌套循环
6. 实现 `__getitem__` 让自定义类支持切片
7. 深拷贝 vs 浅拷贝的区别（写代码验证）
8. 用 `defaultdict` / `Counter` 实现词频统计
9. 实现一个 LRU Cache
10. Python 中的变量作用域问题

---

## 推荐学习资源

### 书籍
1. **《Python编程：从入门到实践》** — 入门首选
2. **《流畅的Python》**（Fluent Python）— 进阶必备，必读
3. **《Python Cookbook》** — 实战技巧大全
4. **《Effective Python》** — 90条最佳实践

### 在线资源
- **Python 官方文档**（docs.python.org）— 最终的参考答案
- **LeetCode** — 用 Python 刷题巩固
- **Real Python**（realpython.com）— 高质量教程
- **PEP 8**（python.org/dev/peps/pep-0008）

### 刷题路径
1. 先用 Python 重新刷你已经做过的 C++ 算法题
2. 重点练习字符串、哈希表、双指针类的 Python 简洁写法
3. 练习用 Python 一行代码解决的问题（列表推导式、lambda）

---

> **最后忠告**：精通 Python 不是背诵所有特性，而是**理解其设计哲学**（Pythonic），
> 写出简洁、可读、高效的代码。多看优秀源码，多动手写，多对比 C++ 和 Python 的异同。
> 祝你面试顺利！🎯
