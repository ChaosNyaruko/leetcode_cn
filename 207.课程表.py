#
# @lc app=leetcode.cn id=207 lang=python3
#
# [207] 课程表
#
# https://leetcode-cn.com/problems/course-schedule/description/
#
# algorithms
# Medium (54.50%)
# Likes:    657
# Dislikes: 0
# Total Accepted:    85.5K
# Total Submissions: 156.8K
# Testcase Example:  '2\n[[1,0]]'
#
# 你这个学期必须选修 numCourse 门课程，记为 0 到 numCourse-1 。
#
# 在选修某些课程之前需要一些先修课程。 例如，想要学习课程 0 ，你需要先完成课程 1 ，我们用一个匹配来表示他们：[0,1]
#
# 给定课程总量以及它们的先决条件，请你判断是否可能完成所有课程的学习？
#
#
#
# 示例 1:
#
# 输入: 2, [[1,0]]
# 输出: true
# 解释: 总共有 2 门课程。学习课程 1 之前，你需要完成课程 0。所以这是可能的。
#
# 示例 2:
#
# 输入: 2, [[1,0],[0,1]]
# 输出: false
# 解释: 总共有 2 门课程。学习课程 1 之前，你需要先完成​课程 0；并且学习课程 0 之前，你还应先完成课程 1。这是不可能的。
#
#
#
# 提示：
#
#
# 输入的先决条件是由 边缘列表 表示的图形，而不是 邻接矩阵 。详情请参见图的表示法。
# 你可以假定输入的先决条件中没有重复的边。
# 1 <= numCourses <= 10^5
#
#
#

# @lc code=start
class Solution:
    # def canFinish(self, numCourses: int, prerequisites) -> bool:
    def canFinish_dfs(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        edges = collections.defaultdict(list)
        valid = True
        visited = [0] * numCourses

        for edge in prerequisites:
            edges[edge[1]].append(edge[0])

        def dfs(u):
            nonlocal valid
            visited[u] = 1
            for v in edges[u]:
                if visited[v] == 0:
                    dfs(v)
                    if not valid:
                        return
                elif visited[v] == 1:
                    valid = False
                    return
            visited[u] = 2
            return
        for i in range(0, numCourses):
            if not valid:
                break
            assert visited[i] != 1
            if visited[i] == 0:
                dfs(i)
        return valid

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # bfs
        edges = collections.defaultdict(list)
        indegrees = [0] * numCourses

        for edge in prerequisites:
            edges[edge[1]].append(edge[0])
            indegrees[edge[0]] += 1

        q = collections.deque([u for u in range(0, numCourses) if indegrees[u] == 0])

        visited = 0
        while q:
            visited += 1
            u = q.popleft()
            for out in edges[u]:
                indegrees[out] -= 1
                if indegrees[out] == 0:
                    q.append(out)
        return visited == numCourses

# @lc code=end

