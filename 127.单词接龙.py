#
# @lc app=leetcode.cn id=127 lang=python3
#
# [127] 单词接龙
#

# @lc code=start
class Solution:
    def ladderLength_1(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        q = collections.deque()
        dic = set(wordList)
        ladder = 1
        q.append(beginWord)
        while q:
            # n = len(q)
            for _ in range(len(q), 0, -1):
                cur = q.popleft()
                if cur == endWord:
                    return ladder
                dic.discard(cur)
                for i in range(len(cur)):
                    for j in range(26):
                        tmp = cur[:i] + chr(ord("a") + j) + cur[i + 1:] 
                        # print(cur, tmp)
                        if tmp in dic:
                            q.append(tmp)
                            # print("push", cur, tmp, ladder)
            # print("queue", cur, q, "ladder", ladder)
            ladder += 1

        return 0

    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        dic = set(wordList)
        if endWord not in dic:
            return 0
        head = set()
        tail = set()
        head.add(beginWord)
        tail.add(endWord)
        ladder = 2
        while head and tail:
            if len(head) > len(tail):
                head, tail = tail, head
            tmp = set()
            for word in head:
                for i in range(len(word)):
                    for j in range(26):
                        c = word[:i] + chr(ord("a") + j) + word[i + 1:]
                        if c in tail:
                            return ladder
                        if c in dic:
                            tmp.add(c)
                            dic.remove(c)
            ladder += 1
            head = tmp.copy()
        return 0
            
            
# @lc code=end

