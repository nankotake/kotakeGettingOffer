# 给定一个单词列表 words 和一个整数 k ，返回前 k 个出现次数最多的单词。
# 返回的答案应该按单词出现频率由高到低排序。如果不同的单词有相同出现频率， 按字典顺序 排序。
 
# 示例 1：
# 输入: words = ["i", "love", "leetcode", "i", "love", "coding"], k = 2
# 输出: ["i", "love"]
# 解析: "i" 和 "love" 为出现次数最多的两个单词，均为2次。
#     注意，按字母顺序 "i" 在 "love" 之前。
# 示例 2：
# 输入: ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], k = 4
# 输出: ["the", "is", "sunny", "day"]
# 解析: "the", "is", "sunny" 和 "day" 是出现次数最多的四个单词，
#     出现次数依次为 4, 3, 2 和 1 次。
 
# 注意：
# 1 <= words.length <= 500
# 1 <= words[i].length <= 10
# words[i] 由小写英文字母组成。
# k 的取值范围是 [1, 不同 words[i] 的数量]

from collections import defaultdict

words = ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is", "is"]
k = 4

wordList = []
cntList = []

wordDict = defaultdict(int)

for i in words:
    wordDict[i]+=1

# for i in words:
#     if i in wordList:
#         for j in len(wordList):
#             if wordList[j] == i:
#                 cntList[j]+=1
#     else:
#         wordList.append(i)
#         cntList.append(1)

wordList = wordDict.keys()
# wordList.sort(key=lambda x : wordDict[x])
wordList = sorted(wordList, key=lambda x : (-wordDict[x],x))
# wordList.sort(key=lambda x : cntList[x])

print(wordList[0:k])