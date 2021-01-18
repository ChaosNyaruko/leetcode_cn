#
# @lc app=leetcode.cn id=721 lang=python3
#
# [721] 账户合并
#

# @lc code=start
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        emailToIndex = dict()
        emailToName = dict()
        for account in accounts:
            name = account[0]
            for email in account[1:]:
                if email not in emailToIndex:
                    emailToIndex[email] = len(emailToIndex)
                    emailToName[email] = name
        
        parent = [i for i in range(len(emailToIndex))]
        # print(parent)
        def find(x):
            if x != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]
        def union(x, y):
            rx, ry = find(x), find(y)
            if rx != ry:
                parent[ry] = rx
            return

        for account in accounts:
            firstIndex = emailToIndex[account[1]]
            for a in account[2:]:
                union(firstIndex, emailToIndex[a])
        
        indexToEmails = collections.defaultdict(list)
        for email, index in emailToIndex.items():
            index = find(index)
            indexToEmails[index].append(email)
        
        res = list()
        for emails in indexToEmails.values():
            res.append([emailToName[emails[0]]] + sorted(emails)) 
        return res
# @lc code=end

