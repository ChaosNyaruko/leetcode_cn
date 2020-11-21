/*
 * @lc app=leetcode.cn id=56 lang=golang
 *
 * [56] 合并区间
 *
 * https://leetcode-cn.com/problems/merge-intervals/description/
 *
 * algorithms
 * Medium (43.42%)
 * Likes:    701
 * Dislikes: 0
 * Total Accepted:    165.7K
 * Total Submissions: 381.7K
 * Testcase Example:  '[[1,3],[2,6],[8,10],[15,18]]'
 *
 * 给出一个区间的集合，请合并所有重叠的区间。
 * 
 * 
 * 
 * 示例 1:
 * 
 * 输入: intervals = [[1,3],[2,6],[8,10],[15,18]]
 * 输出: [[1,6],[8,10],[15,18]]
 * 解释: 区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].
 * 
 * 
 * 示例 2:
 * 
 * 输入: intervals = [[1,4],[4,5]]
 * 输出: [[1,5]]
 * 解释: 区间 [1,4] 和 [4,5] 可被视为重叠区间。
 * 
 * 注意：输入类型已于2019年4月15日更改。 请重置默认代码定义以获取新方法签名。
 * 
 * 
 * 
 * 提示：
 * 
 * 
 * intervals[i][0] <= intervals[i][1]
 * 
 * 
 */

// @lc code=start
type myIntervals [][]int

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}
func (is myIntervals) Len() int{
	return len(is)
}

func (is myIntervals) Swap(i, j int) {
	is[i], is[j] = is[j],is[i]
}

func (is myIntervals) Less(i, j int) bool {
	if is[i][0] == is[j][0] {
		return is[i][1] < is[j][1]
	} 
	return is[i][0] < is[j][0]
}

func merge(intervals [][]int) [][]int {
	m := myIntervals(intervals)
	sort.Sort(m)
	res := make([][]int, 0, len(intervals))
	if len(intervals) == 0 {
		return res
	}
	res = append(res, intervals[0])
	for i:=1; i < len(m); i++  {
		last := res[len(res) - 1]
		if m[i][0] <= last[1] {
			last[1] = max(m[i][1], last[1])
		} else {
			res = append(res, m[i])
		}
	}
	return res
}
// @lc code=end

