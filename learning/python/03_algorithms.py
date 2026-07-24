"""
第三阶段：算法与数据结构（Python 实现）
对照你的 C++ 算法储备，用 Python 重写常见算法
"""

from collections import deque, Counter, defaultdict, OrderedDict
import heapq
import bisect


# ==================== 1. collections 高阶数据结构 ====================
print("=" * 60)
print("=== collections 模块 ===")
print("=" * 60)


# 1.1 deque：双端队列（用作栈/队列）
def deque_example():
    dq = deque()
    # 作为队列（FIFO）
    dq.append(1)          # 右端入队
    dq.append(2)
    dq.append(3)
    print(f"队列出队: {dq.popleft()}")  # 1, O(1)

    # 作为栈（LIFO）
    dq.append(4)
    print(f"栈出栈: {dq.pop()}")  # 4, O(1)

    # 双端操作
    dq.appendleft(0)       # 左端入队
    print(f"左端出队: {dq.popleft()}")  # 0

    # 旋转（面试有用）
    dq = deque([1, 2, 3, 4, 5])
    dq.rotate(2)  # 右移2位
    print(f"旋转后: {list(dq)}")  # [4, 5, 1, 2, 3]


deque_example()


# 1.2 Counter：计数器
def counter_example():
    # 统计字符频率（面试高频）
    s = "hello world"
    cnt = Counter(s)
    print(f"字符频率: {cnt}")
    print(f"最常见的3个: {cnt.most_common(3)}")

    # 计数运算
    cnt1 = Counter(['a', 'b', 'c', 'a', 'b'])
    cnt2 = Counter(['a', 'b', 'b', 'd'])
    print(f"相加: {cnt1 + cnt2}")
    print(f"相减: {cnt1 - cnt2}")  # 只保留正数
    print(f"交集: {cnt1 & cnt2}")
    print(f"并集: {cnt1 | cnt2}")


counter_example()


# 1.3 defaultdict：带默认值的字典
def defaultdict_example():
    # 分组（面试高频）
    words = ["apple", "banana", "avocado", "blueberry", "cherry"]
    
    # 按首字母分组
    groups = defaultdict(list)
    for word in words:
        groups[word[0]].append(word)
    print(f"按首字母分组: {dict(groups)}")

    # 计数（替代 Counter 的另一种方式）
    freq = defaultdict(int)
    for ch in "hello":
        freq[ch] += 1
    print(f"频率统计: {dict(freq)}")


defaultdict_example()


# ==================== 2. heapq：堆 ====================
print("\n" + "=" * 60)
print("=== heapq：堆（优先队列）===")
print("=" * 60)


def heap_example():
    arr = [3, 1, 4, 1, 5, 9, 2, 6]
    heapq.heapify(arr)  # 原地建堆（最小堆）
    print(f"堆顶: {arr[0]}")  # 最小值

    # 弹出堆顶
    smallest = heapq.heappop(arr)
    print(f"弹出最小: {smallest}")

    # 压入新元素
    heapq.heappush(arr, 0)

    # 弹出并压入（组合操作）
    result = heapq.heappushpop(arr, -1)  # 先压入-1，再弹出最小
    print(f"pushpop 结果: {result}")

    # 获取最大的K个元素（面试高频）
    arr2 = [3, 1, 4, 1, 5, 9, 2, 6]
    print(f"最大的3个: {heapq.nlargest(3, arr2)}")
    print(f"最小的3个: {heapq.nsmallest(3, arr2)}")


heap_example()


# ==================== 3. bisect：二分查找 ====================
print("\n" + "=" * 60)
print("=== bisect：二分查找 ===")
print("=" * 60)


def bisect_example():
    arr = [1, 3, 5, 7, 9]

    # bisect_left：找到插入位置（如果存在相同元素，插入到左边）
    pos = bisect.bisect_left(arr, 6)
    print(f"6 应插入到位置: {pos}")  # 3

    # bisect_right / bisect：找到插入位置（存在相同元素，插入到右边）
    pos = bisect.bisect_right(arr, 5)
    print(f"5 插入到右边位置: {pos}")  # 3

    # insort：插入并保持有序
    arr2 = [1, 3, 5, 7]
    bisect.insort(arr2, 4)
    print(f"插入后: {arr2}")  # [1, 3, 4, 5, 7]


bisect_example()


# ==================== 4. 常见算法模板 ====================
print("\n" + "=" * 60)
print("=== Python 算法模板 ===")
print("=" * 60)


# 4.1 二叉树
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BinaryTree:
    @staticmethod
    def inorder_traversal_recursive(root):
        """递归中序遍历"""
        if not root:
            return []
        return (BinaryTree.inorder_traversal_recursive(root.left)
                + [root.val]
                + BinaryTree.inorder_traversal_recursive(root.right))

    @staticmethod
    def inorder_traversal_iterative(root):
        """迭代中序遍历（栈）"""
        result = []
        stack = []
        curr = root
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            result.append(curr.val)
            curr = curr.right
        return result

    @staticmethod
    def level_order(root):
        """层序遍历（BFS）"""
        if not root:
            return []
        result = []
        queue = deque([root])
        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(level)
        return result


# 构建测试二叉树
#     1
#    / \
#   2   3
#  / \
# 4   5
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

bt = BinaryTree()
print(f"递归中序: {bt.inorder_traversal_recursive(root)}")
print(f"迭代中序: {bt.inorder_traversal_iterative(root)}")
print(f"层序遍历: {bt.level_order(root)}")


# 4.2 图的 DFS / BFS
class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)  # 无向图

    def dfs_recursive(self, start, visited=None):
        if visited is None:
            visited = set()
        visited.add(start)
        print(start, end=" ")
        for neighbor in self.graph[start]:
            if neighbor not in visited:
                self.dfs_recursive(neighbor, visited)

    def bfs(self, start):
        visited = {start}
        queue = deque([start])
        result = []
        while queue:
            node = queue.popleft()
            result.append(node)
            for neighbor in self.graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        return result


g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 3)
print("\nDFS:", end=" ")
g.dfs_recursive(0)
print(f"\nBFS: {g.bfs(0)}")


# 4.3 并查集 Union-Find
class UnionFind:
    """并查集（面试高频）"""
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        """路径压缩"""
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        """按秩合并"""
        px, py = self.find(x), self.find(y)
        if px == py:
            return False
        if self.rank[px] < self.rank[py]:
            self.parent[px] = py
        elif self.rank[px] > self.rank[py]:
            self.parent[py] = px
        else:
            self.parent[py] = px
            self.rank[px] += 1
        return True

    def connected(self, x, y):
        return self.find(x) == self.find(y)


uf = UnionFind(5)
uf.union(0, 1)
uf.union(1, 2)
uf.union(3, 4)
print(f"0和2是否连通: {uf.connected(0, 2)}")  # True
print(f"0和3是否连通: {uf.connected(0, 3)}")  # False


# 4.4 字典树 Trie
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False


class Trie:
    """字典树 / 前缀树（面试高频）"""
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.is_end = True

    def search(self, word: str) -> bool:
        node = self.root
        for ch in word:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return node.is_end

    def starts_with(self, prefix: str) -> bool:
        """是否存在以 prefix 为前缀的单词"""
        node = self.root
        for ch in prefix:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return True

    def autocomplete(self, prefix: str) -> list:
        """自动补全（扩展）"""
        def dfs(node, path):
            if node.is_end:
                result.append("".join(path))
            for ch, child in node.children.items():
                path.append(ch)
                dfs(child, path)
                path.pop()

        node = self.root
        for ch in prefix:
            if ch not in node.children:
                return []
            node = node.children[ch]

        result = []
        dfs(node, list(prefix))
        return result


trie = Trie()
trie.insert("apple")
trie.insert("app")
trie.insert("application")
trie.insert("banana")
print(f"search('app'): {trie.search('app')}")           # True
print(f"search('apple'): {trie.search('apple')}")       # True
print(f"search('appl'): {trie.search('appl')}")         # False
print(f"starts_with('app'): {trie.starts_with('app')}")  # True
print(f"autocomplete('app'): {trie.autocomplete('app')}")


# 4.5 二分搜索模板
def binary_search(nums: list, target: int) -> int:
    """标准二分查找"""
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


def lower_bound(nums: list, target: int) -> int:
    """第一个 >= target 的位置（C++ lower_bound）"""
    left, right = 0, len(nums)
    while left < right:
        mid = left + (right - left) // 2
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid
    return left


def upper_bound(nums: list, target: int) -> int:
    """第一个 > target 的位置（C++ upper_bound）"""
    left, right = 0, len(nums)
    while left < right:
        mid = left + (right - left) // 2
        if nums[mid] <= target:
            left = mid + 1
        else:
            right = mid
    return left


arr = [1, 2, 2, 2, 3, 4, 5]
print(f"\nbinary_search(2): {binary_search(arr, 2)}")
print(f"lower_bound(2): {lower_bound(arr, 2)}")  # 1
print(f"upper_bound(2): {upper_bound(arr, 2)}")  # 4


# 4.6 回溯框架
def backtrack_example():
    """全排列（回溯算法模板）"""
    def permute(nums):
        result = []

        def backtrack(path, remaining):
            if not remaining:
                result.append(path[:])  # 深拷贝
                return
            for i, num in enumerate(remaining):
                path.append(num)
                backtrack(path, remaining[:i] + remaining[i+1:])
                path.pop()

        backtrack([], nums)
        return result

    print(f"全排列 [1,2,3]: {permute([1, 2, 3])}")


backtrack_example()


# 4.7 前缀和与差分
def prefix_sum_example():
    """前缀和模板"""
    nums = [1, 2, 3, 4, 5]
    prefix = [0]
    for num in nums:
        prefix.append(prefix[-1] + num)
    # prefix[i] = nums[0] + ... + nums[i-1]
    # sum(nums[l:r]) = prefix[r] - prefix[l]
    print(f"前缀和: {prefix}")
    print(f"nums[1:4]的和: {prefix[4] - prefix[1]}")  # 2+3+4=9


prefix_sum_example()


# ==================== 5. 正则表达式 ====================
print("\n" + "=" * 60)
print("=== 正则表达式 ===")
print("=" * 60)

import re

def regex_example():
    text = "我的邮箱是 alice@example.com，电话是 138-0000-0001"

    # 查找邮箱
    email_pattern = r'\w+@\w+\.\w+'
    email = re.search(email_pattern, text)
    if email:
        print(f"邮箱: {email.group()}")

    # 查找所有手机号
    phone_pattern = r'\d{3}-\d{4}-\d{4}'
    phones = re.findall(phone_pattern, text)
    print(f"手机号: {phones}")

    # 替换
    result = re.sub(r'\d{3}-\d{4}-\d{4}', '***-****-****', text)
    print(f"脱敏后: {result}")

    # 分割
    print(re.split(r'[，。；]', "你好，世界。再见；朋友"))


regex_example()
