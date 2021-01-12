#
# @lc app=leetcode.cn id=1203 lang=python3
#
# [1203] 项目管理
#

# @lc code=start
class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        def topSort(graph, indegree, items) -> List:
            q = collections.deque()
            for item in items:
                if indegree[item] == 0:
                    q.append(item)
            
            orders = []
            while q:
                src = q.popleft()
                orders.append(src)
                for dst in graph[src]:
                    indegree[dst] -= 1
                    if indegree[dst] == 0:
                        q.append(dst)
                
            return orders
        # we use m + n becuase we may tranfer item[i] groupId=-1 -> groudId=m+i
        groupItem = [[] for _ in range(m + n)]
        for i in range(len(group)):
            if group[i] == -1:
                group[i] = m + i
            groupItem[group[i]].append(i)
        
        groupGraph = [[] for _ in range(m + n)]
        groupDegree = [0 for  _ in range(m + n)]
        itemGraph = [[] for  _ in range(n)]
        itemDegree = [0 for _ in range(n)]

        for curItem in range(len(beforeItems)):
            beforeCur = beforeItems[curItem]
            curGroupId = group[curItem]
            for item in beforeCur:
                preGroupID = group[item]
                if preGroupID != curGroupId: # inter groups
                    groupGraph[preGroupID].append(curGroupId)
                    groupDegree[curGroupId] += 1
                else: # inside a group
                    itemGraph[item].append(curItem)
                    itemDegree[curItem] += 1

        # topSort among groups
        groups = [i for i in range(m + n)]
        groupOrders = topSort(groupGraph, groupDegree, groups)
        if len(groupOrders) < len(groups):
            return []

        res = []
        for g in groupOrders:
            items = groupItem[g]
            orders = topSort(itemGraph, itemDegree, items)
            if len(orders) < len(items):
                return []
            res.extend(orders)
        return res
            
# @lc code=end


func topSort(graph [][]int, deg, items []int) (orders []int) {
    q := []int{}
    for _, i := range items {
        if deg[i] == 0 {
            q = append(q, i)
        }
    }
    for len(q) > 0 {
        from := q[0]
        q = q[1:]
        orders = append(orders, from)
        for _, to := range graph[from] {
            deg[to]--
            if deg[to] == 0 {
                q = append(q, to)
            }
        }
    }
    return
}

func sortItems(n, m int, group []int, beforeItems [][]int) (ans []int) {
    groupItems := make([][]int, m+n) // groupItems[i] 表示第 i 个组负责的项目列表
    for i := range group {
        if group[i] == -1 {
            group[i] = m + i // 给不属于任何组的项目分配一个组
        }
        groupItems[group[i]] = append(groupItems[group[i]], i)
    }

    groupGraph := make([][]int, m+n) // 组间依赖关系
    groupDegree := make([]int, m+n)
    itemGraph := make([][]int, n) // 组内依赖关系
    itemDegree := make([]int, n)
    for cur, items := range beforeItems {
        curGroupID := group[cur]
        for _, pre := range items {
            preGroupID := group[pre]
            if preGroupID != curGroupID { // 不同组项目，确定组间依赖关系
                groupGraph[preGroupID] = append(groupGraph[preGroupID], curGroupID)
                groupDegree[curGroupID]++
            } else { // 同组项目，确定组内依赖关系
                itemGraph[pre] = append(itemGraph[pre], cur)
                itemDegree[cur]++
            }
        }
    }

    // 组间拓扑序
    items := make([]int, m+n)
    for i := range items {
        items[i] = i
    }
    groupOrders := topSort(groupGraph, groupDegree, items)
    if len(groupOrders) < len(items) {
        return nil
    }

    // 按照组间的拓扑序，依次求得各个组的组内拓扑序，构成答案
    for _, groupID := range groupOrders {
        items := groupItems[groupID]
        orders := topSort(itemGraph, itemDegree, items)
        if len(orders) < len(items) {
            return nil
        }
        ans = append(ans, orders...)
    }
    return
}
