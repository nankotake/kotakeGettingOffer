"""
第三阶段：进阶数据操作与面试算法
涵盖：collections 模块、堆、二分、排序、算法模板、正则表达式
"""
from collections import deque, Counter, defaultdict, OrderedDict
import heapq
import bisect
import re
from typing import List, Optional


# ==================== 1. collections 模块 ====================
print("=" * 50)
print("=== collections 模块 ===")
print("=" * 50)


# 1.1 deque — 双端队列（O(1) 在两端插入/删除）
print("\n--- deque ---")

# 列表做栈（append + pop）是 O(1)，做队列（pop(0)）是 O(n)
# deque 两端操作都是 O(1)

dq = deque([1, 2, 3])
dq.append(4)          # 右侧添加 → [1, 2, 3, 4]
dq.appendleft(0)      # 左侧添加 → [0, 1, 2, 3, 4]
dq.pop()              # 右侧弹出 → 4
dq.popleft()          # 左侧弹出 → 0
print(f"deque: {dq}")  # [1, 2, 3]

# 限制长度的 deque
dq_limited = deque(maxlen=3)
dq_limited.extend([1, 2, 3, 4, 5])  # 只保留最后3个
print(f"限制长度: {dq_limited}")     # [3, 4, 5]

# 实战：用 deque 实现 BFS 队列


# 1.2 Counter — 频率统计（面试必考！）
print("\n--- Counter ---")

words = "hello world hello python hello".split()
word_count = Counter(words)
print(f"词频: {word_count}")                    # {'hello': 3, 'world': 1, 'python': 1}
print(f"最常见2个: {word_count.most_common(2)}")  # [('hello', 3), ...]

# Counter 运算
c1 = Counter(a=3, b=1)
c2 = Counter(a=1, b=2)
print(f"c1 + c2: {c1 + c2}")   # 相加
print(f"c1 - c2: {c1 - c2}")   # 相减（结果只保留正数）
print(f"c1 & c2: {c1 & c2}")   # 取 min
print(f"c1 | c2: {c1 | c2}")   # 取 max

# 实战面试题：判断两个字符串是否为字母异位词
def is_anagram(s1: str, s2: str) -> bool:
    """用 Counter 精确判断 anagram（面试推荐写法）"""
    return Counter(s1) == Counter(s2)

print(f"anagram 'listen' vs 'silent': {is_anagram('listen', 'silent')}")  # True


# 1.3 defaultdict — 默认值字典（面试必考！）
print("\n--- defaultdict ---")

# 传统写法需要检查 key 是否存在
# 用 defaultdict 自动给新 key 赋默认值
dd_list = defaultdict(list)
dd_list["fruits"].append("apple")
dd_list["fruits"].append("banana")
print(f"defaultdict(list): {dict(dd_list)}")  # {'fruits': ['apple', 'banana']}

dd_int = defaultdict(int)
for ch in "mississippi":
    dd_int[ch] += 1   # 不需要检查 key 是否存在
print(f"字符计数: {dict(dd_int)}")

# 实战：分组（面试高频）
students = [("Alice", "A"), ("Bob", "B"), ("Charlie", "A"), ("David", "B")]
by_grade = defaultdict(list)
for name, grade in students:
    by_grade[grade].append(name)
print(f"按等级分组: {dict(by_grade)}")

# 实战：图的邻接表
graph = defaultdict(set)
edges = [(1, 2), (2, 3), (1, 3)]
for u, v in edges:
    graph[u].add(v)
    graph[v].add(u)  # 无向图
print(f"邻接表: {dict(graph)}")


# 1.4 OrderedDict — 有序字典
print("\n--- OrderedDict ---")
# Python 3.7+ 内置 dict 已经保持插入顺序
# OrderedDict 额外提供：reorder、move_to_end
od = OrderedDict()
od["a"] = 1
od["b"] = 2
od["c"] = 3
od.move_to_end("a")          # 把 "a" 移到最后
print(f"move_to_end('a'): {od}")
od.move_to_end("c", last=False)  # 把 "c" 移到最前
print(f"move_to_end('c', False): {od}")
print(f"popitem(last=False): {od.popitem(last=False)}")  # 弹出第一个


# ==================== 2. heapq — 堆（优先队列） ====================
print("\n" + "=" * 50)
print("=== heapq ===")
print("=" * 50)

# heapq 默认是最小堆
nums = [3, 1, 4, 1, 5, 9, 2, 6]
heapq.heapify(nums)  # 原地转堆，O(n)
print(f"堆化后: {nums}")  # [1, 1, 2, 3, 5, 9, 4, 6]

heapq.heappush(nums, 0)   # 插入
print(f"push 0: {heapq.heappop(nums)}")  # 弹出最小: 0
print(f"堆顶（最小）: {nums[0]}")        # 访问堆顶: 1

# 最大堆（取反技巧）
max_heap = [-x for x in [3, 1, 4, 1, 5]]
heapq.heapify(max_heap)
print(f"最大堆堆顶: {-heapq.heappop(max_heap)}")  # 5

# nlargest / nsmallest
data = [3, 1, 4, 1, 5, 9, 2, 6]
print(f"Top 3 最大: {heapq.nlargest(3, data)}")  # [9, 6, 5]
print(f"Top 3 最小: {heapq.nsmallest(3, data)}")  # [1, 1, 2]

# 实战：合并 K 个有序列表（LeetCode 23）
def merge_k_sorted(lists: List[List[int]]) -> List[int]:
    """用堆合并 K 个有序列表"""
    heap = []
    for i, lst in enumerate(lists):
        if lst:
            # (值, 列表索引, 元素索引) — 元素索引用于处理重复值
            heapq.heappush(heap, (lst[0], i, 0))

    result = []
    while heap:
        val, list_idx, elem_idx = heapq.heappop(heap)
        result.append(val)
        if elem_idx + 1 < len(lists[list_idx]):
            heapq.heappush(heap, (lists[list_idx][elem_idx + 1], list_idx, elem_idx + 1))
    return result

print(f"合并K有序: {merge_k_sorted([[1,4,5],[1,3,4],[2,6]])}")

# 实战：用堆实现 Top K（LeetCode 215, 347）
def top_k_frequent(nums: List[int], k: int) -> List[int]:
    """前 K 个高频元素（heap 典型应用）"""
    count = Counter(nums)
    # 最小堆维护当前 top-k；只存 k 个，堆 size = k → O(n log k)
    heap = []
    for num, freq in count.items():
        heapq.heappush(heap, (freq, num))
        if len(heap) > k:
            heapq.heappop(heap)  # 踢掉频率最小的
    return [num for _, num in heap]

print(f"Top-2 高频: {top_k_frequent([1,1,1,2,2,3], 2)}")

# 实战：Dijkstra 最短路径（面试里的堆核心用途）
def dijkstra_demo():
    """用堆实现 Dijkstra 最短路径"""
    n = 5
    graph = defaultdict(list)
    edges = [(0, 1, 2), (0, 2, 4), (1, 2, 1), (1, 3, 7), (2, 3, 3), (3, 4, 1)]
    for u, v, w in edges:
        graph[u].append((v, w))
        graph[v].append((u, w))

    dist = [float('inf')] * n
    dist[0] = 0
    heap = [(0, 0)]  # (距离, 节点)

    while heap:
        d, u = heapq.heappop(heap)
        if d > dist[u]:
            continue  # 过期的最短距离，跳过
        for v, w in graph[u]:
            new_dist = d + w
            if new_dist < dist[v]:
                dist[v] = new_dist
                heapq.heappush(heap, (new_dist, v))

    print(f"节点0到各点最短距离: {dist}")

dijkstra_demo()


# ==================== 3. bisect — 二分查找 ====================
print("\n" + "=" * 50)
print("=== bisect 二分查找 ===")
print("=" * 50)

arr = [1, 3, 5, 7, 9]
print(f"bisect_left(5):  {bisect.bisect_left(arr, 5)}")   # 2（第一个≥5 的位置）
print(f"bisect_right(5): {bisect.bisect_right(arr, 5)}")  # 3（第一个>5 的位置）

# 插入并保持有序
bisect.insort(arr, 6)  # O(n) 因为要移动元素
print(f"insort(6): {arr}")  # [1, 3, 5, 6, 7, 9]

# 实战：在排序数组中找范围（LeetCode 34）
def search_range(nums: List[int], target: int) -> List[int]:
    """在排序数组中查找元素的起始和结束位置"""
    left = bisect.bisect_left(nums, target)
    right = bisect.bisect_right(nums, target) - 1
    if left <= right:
        return [left, right]
    return [-1, -1]

print(f"5 的范围: {search_range([5,7,7,8,8,10], 8)}")  # [3, 4]

# 实战：最长递增子序列长度（LeetCode 300，bisect 经典应用）
def length_of_lis(nums: List[int]) -> int:
    """O(n log n) 求最长递增子序列长度"""
    tails = []  # tails[i] = 长度为 i+1 的递增子序列的最小末尾值
    for x in nums:
        i = bisect.bisect_left(tails, x)
        if i == len(tails):
            tails.append(x)
        else:
            tails[i] = x
    return len(tails)

print(f"LIS 长度: {length_of_lis([10,9,2,5,3,7,101,18])}")  # 4


# ==================== 4. 排序技巧 ====================
print("\n" + "=" * 50)
print("=== 排序技巧 ===")
print("=" * 50)

# sorted() 返回新列表，list.sort() 原地排序
arr = [3, 1, 4, 1, 5]
print(f"sorted(): {sorted(arr)}, 原: {arr}")  # 原列表不变
arr.sort()
print(f"sort():   {arr}")  # 原列表已排序

# 自定义 key（面试高频）
# 按成绩降序排列学生
students = [("Alice", 85), ("Bob", 92), ("Charlie", 78)]
sorted_students = sorted(students, key=lambda x: x[1], reverse=True)
print(f"按成绩降序: {sorted_students}")

# 多级排序：先按等级，再按成绩降序
records = [("A", 85), ("B", 92), ("A", 78), ("B", 85)]
records.sort(key=lambda x: (x[0], -x[1]))  # 等级升序，成绩降序
print(f"多级排序: {records}")

# 用 tuple 的默认比较实现多级排序
# (等级, -成绩)：等级低的在前，同等级成绩高的在前
records2 = sorted(records, key=lambda x: (x[0], -x[1]))
print(f"多级排序(sorted): {records2}")

# 按字符串长度排序
words = ["apple", "cat", "banana", "dog"]
print(f"按长度: {sorted(words, key=len)}")

# 按字典值排序（面试高频）
d = {"a": 3, "b": 1, "c": 2}
by_key = sorted(d.items(), key=lambda x: x[0])      # 按键排序
by_value = sorted(d.items(), key=lambda x: x[1])     # 按值排序
print(f"按键:  {by_key}")
print(f"按值:  {by_value}")


# ==================== 5. 算法模板 ====================
print("\n" + "=" * 50)
print("=== 算法模板（Python 实现） ===")
print("=" * 50)


# 5.1 快速排序
def quicksort(arr: List[int]) -> List[int]:
    """快速排序（面试版 — 额外空间，简洁易懂）"""
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

print(f"\n快排: {quicksort([3, 6, 8, 10, 1, 2, 1])}")


def quicksort_inplace(arr: List[int], left: int = 0, right: int = None):
    """快速排序（原地版 — 面试推荐）"""
    if right is None:
        right = len(arr) - 1
    if left >= right:
        return

    pivot = arr[(left + right) // 2]
    i, j = left, right
    while i <= j:
        while arr[i] < pivot:
            i += 1
        while arr[j] > pivot:
            j -= 1
        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1

    quicksort_inplace(arr, left, j)
    quicksort_inplace(arr, i, right)

arr_test = [3, 6, 8, 10, 1, 2, 1]
quicksort_inplace(arr_test)
print(f"原地快排: {arr_test}")


# 5.2 归并排序
def mergesort(arr: List[int]) -> List[int]:
    """归并排序"""
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = mergesort(arr[:mid])
    right = mergesort(arr[mid:])
    return merge(left, right)

def merge(left: List[int], right: List[int]) -> List[int]:
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

print(f"归并排序: {mergesort([3, 6, 8, 10, 1, 2, 1])}")


# 5.3 二叉树（定义 + 遍历）
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def build_tree():
    """构建示例树:
          1
         / \
        2   3
       / \   \
      4   5   6
    """
    root = TreeNode(1)
    root.left = TreeNode(2, TreeNode(4), TreeNode(5))
    root.right = TreeNode(3, None, TreeNode(6))
    return root

# 前序遍历（根→左→右）
def preorder(root: Optional[TreeNode]) -> List[int]:
    """前序遍历 — 递归"""
    def dfs(node):
        if not node:
            return
        result.append(node.val)
        dfs(node.left)
        dfs(node.right)
    result = []
    dfs(root)
    return result

def preorder_iter(root: Optional[TreeNode]) -> List[int]:
    """前序遍历 — 迭代（栈）"""
    result = []
    stack = [root]
    while stack:
        node = stack.pop()
        if node:
            result.append(node.val)
            stack.append(node.right)  # 先右后左，pop 时左先出
            stack.append(node.left)
    return result

# 中序遍历（左→根→右）
def inorder(root: Optional[TreeNode]) -> List[int]:
    """中序遍历 — 递归"""
    def dfs(node):
        if not node:
            return
        dfs(node.left)
        result.append(node.val)
        dfs(node.right)
    result = []
    dfs(root)
    return result

def inorder_iter(root: Optional[TreeNode]) -> List[int]:
    """中序遍历 — 迭代"""
    result = []
    stack = []
    node = root
    while stack or node:
        while node:           # 一路向左
            stack.append(node)
            node = node.left
        node = stack.pop()
        result.append(node.val)
        node = node.right
    return result

# 层序遍历
from collections import deque
def level_order(root: Optional[TreeNode]) -> List[List[int]]:
    """层序遍历（BFS，面试高频）"""
    if not root:
        return []
    result = []
    q = deque([root])
    while q:
        level = []
        for _ in range(len(q)):
            node = q.popleft()
            level.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        result.append(level)
    return result

tree = build_tree()
print(f"\n前序（递归）: {preorder(tree)}")
print(f"前序（迭代）: {preorder_iter(tree)}")
print(f"中序（递归）: {inorder(tree)}")
print(f"中序（迭代）: {inorder_iter(tree)}")
print(f"层序遍历:    {level_order(tree)}")


# 5.4 DFS / BFS 图遍历
def dfs_graph(graph, start):
    """深度优先遍历（递归）"""
    visited = set()
    def dfs(node):
        visited.add(node)
        print(node, end=" ")
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor)
    dfs(start)
    return visited

def bfs_graph(graph, start):
    """广度优先遍历（队列）"""
    visited = {start}
    q = deque([start])
    while q:
        node = q.popleft()
        print(node, end=" ")
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                q.append(neighbor)
    return visited

# 示例图:
#    1
#   / \
#  2   3
#  |   |
#  4---5
graph = {
    1: [2, 3],
    2: [1, 4],
    3: [1, 5],
    4: [2, 5],
    5: [3, 4],
}
print(f"\n\nDFS 遍历: ", end="")
dfs_graph(graph, 1)
print(f"\nBFS 遍历: ", end="")
bfs_graph(graph, 1)
print()


# 5.5 动态规划模板
def knapsack_01(weights, values, capacity):
    """0-1 背包问题"""
    n = len(weights)
    # dp[i][w] = 前 i 件物品，容量 w 的最大价值
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        w, v = weights[i - 1], values[i - 1]
        for c in range(capacity + 1):
            if c < w:
                dp[i][c] = dp[i - 1][c]  # 放不下
            else:
                dp[i][c] = max(dp[i - 1][c], dp[i - 1][c - w] + v)
    return dp[n][capacity]

def knapsack_01_1d(weights, values, capacity):
    """0-1 背包 — 一维优化（面试推荐）"""
    dp = [0] * (capacity + 1)
    for w, v in zip(weights, values):
        for c in range(capacity, w - 1, -1):  # 倒序遍历！
            dp[c] = max(dp[c], dp[c - w] + v)
    return dp[capacity]

w = [2, 3, 4, 5]
v = [3, 4, 5, 6]
print(f"\n0-1背包(二维): {knapsack_01(w, v, 8)}")
print(f"0-1背包(一维): {knapsack_01_1d(w, v, 8)}")

# 最长公共子序列 LCS
def lcs(s1: str, s2: str) -> int:
    """最长公共子序列长度"""
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp[m][n]

print(f"LCS('abcde', 'ace'): {lcs('abcde', 'ace')}")  # 3


# 5.6 并查集 Union-Find
class UnionFind:
    """并查集（面试必会）"""
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n       # 按秩合并
        self.count = n            # 连通分量数

    def find(self, x):
        """路径压缩"""
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        """按秩合并"""
        rx, ry = self.find(x), self.find(y)
        if rx == ry:
            return False
        if self.rank[rx] < self.rank[ry]:
            self.parent[rx] = ry
        elif self.rank[rx] > self.rank[ry]:
            self.parent[ry] = rx
        else:
            self.parent[ry] = rx
            self.rank[rx] += 1
        self.count -= 1
        return True

    def connected(self, x, y):
        return self.find(x) == self.find(y)

uf = UnionFind(5)
uf.union(0, 1)
uf.union(1, 2)
uf.union(3, 4)
print(f"\n并查集: 0和2连通? {uf.connected(0, 2)}")  # True
print(f"并查集: 0和3连通? {uf.connected(0, 3)}")  # False
print(f"连通分量数: {uf.count}")                   # 2


# 5.7 字典树 Trie
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:
    """字典树（前缀树）"""
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str):
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.is_end = True

    def search(self, word: str) -> bool:
        """精确搜索"""
        node = self.root
        for ch in word:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return node.is_end

    def starts_with(self, prefix: str) -> bool:
        """是否存在以 prefix 开头的词"""
        node = self.root
        for ch in prefix:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return True

trie = Trie()
for word in ["apple", "app", "banana", "bat"]:
    trie.insert(word)
print(f"\nTrie — search 'app': {trie.search('app')}")         # True
print(f"Trie — search 'appl': {trie.search('appl')}")         # False
print(f"Trie — startsWith 'ba': {trie.starts_with('ba')}")   # True


# 5.8 前缀和与差分
def prefix_sum(nums):
    """前缀和：sum[l:r+1] = prefix[r+1] - prefix[l]"""
    prefix = [0] * (len(nums) + 1)
    for i in range(len(nums)):
        prefix[i + 1] = prefix[i] + nums[i]
    return prefix

def range_sum(prefix, l, r):
    """O(1) 求区间 [l, r] 的和"""
    return prefix[r + 1] - prefix[l]

arr = [1, 2, 3, 4, 5]
ps = prefix_sum(arr)
print(f"\n前缀和 sum(1..3): {range_sum(ps, 1, 3)}")  # 2+3+4 = 9

# 二维前缀和
def prefix_sum_2d(matrix):
    """二维前缀和"""
    m, n = len(matrix), len(matrix[0])
    prefix = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(m):
        for j in range(n):
            prefix[i + 1][j + 1] = (
                prefix[i][j + 1]
                + prefix[i + 1][j]
                - prefix[i][j]
                + matrix[i][j]
            )
    return prefix

mat = [[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]]
ps2d = prefix_sum_2d(mat)
# 求 (1,1) 到 (2,2) 的和: 5+6+8+9 = 28
def sum_2d(prefix, r1, c1, r2, c2):
    return (prefix[r2 + 1][c2 + 1]
            - prefix[r1][c2 + 1]
            - prefix[r2 + 1][c1]
            + prefix[r1][c1])

print(f"二维前缀和 (1,1)-(2,2): {sum_2d(ps2d, 1, 1, 2, 2)}")  # 28


# ==================== 6. 正则表达式 re 模块 ====================
print("\n" + "=" * 50)
print("=== 正则表达式 ===")
print("=" * 50)

text = "联系方式: alice@example.com, 手机: 138-1234-5678"
# re.search — 找到第一个匹配
match = re.search(r"\d{3}-\d{4}-\d{4}", text)
if match:
    print(f"search 手机号: {match.group()}")
# re.findall — 返回所有匹配
emails = re.findall(r"\w+@\w+\.\w+", text)
print(f"findall 邮箱: {emails}")
# re.match — 从字符串开头匹配
print(f"match 开头: {re.match(r'联系方式', text)}")
# re.sub — 替换
masked = re.sub(r"\d{3}-\d{4}-\d{4}", "***-****-****", text)
print(f"sub 脱敏: {masked}")
# re.split — 按正则分割
print(f"split: {re.split(r'[:,] ', text)}")

# 常见面试正则
# 匹配 IPv4: \d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}
# 匹配邮箱:  [\w\.-]+@[\w\.-]+\.\w+
# 匹配 URL:  https?://[\w\.-]+(/\S*)?
# 匹配中文:  [一-鿿]+
ip_regex = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
print(f"IPv4: {re.findall(ip_regex, 'ip: 192.168.1.1')}")

# ==================== 7. 字符串比大小原理 ====================
print("\n" + "=" * 50)
print("=== 字符串比大小 ===")
print("=" * 50)

# Python 字符串按字典序逐字符比较 Unicode 码点
print(f"'abc' < 'abd': {'abc' < 'abd'}")    # True
print(f"'abc' < 'abcd': {'abc' < 'abcd'}")  # True（短串是长串前缀）
print(f"ord('a') = {ord('a')}, ord('A') = {ord('A')}")  # 97 vs 65
print(f"'A' < 'a': {'A' < 'a'}")             # True（大写 < 小写）
print(f"'1' < '2': {'1' < '2'}")             # True（数字字符）
print(f"'10' < '2': {'10' < '2'}")           # True（字典序！'1'得码点小于'2'）

# 如何做自然排序（"10" 排在 "2" 后面）？
import re
files = ["file2.txt", "file10.txt", "file1.txt"]
files.sort(key=lambda x: int(re.search(r'\d+', x).group()))
print(f"自然排序: {files}")  # ['file1.txt', 'file2.txt', 'file10.txt']

print("\n" + "=" * 50)
print("第三阶段结束")
print("=" * 50)
