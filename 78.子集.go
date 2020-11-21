/*
 * @lc app=leetcode.cn id=78 lang=golang
 *
 * [78] 子集
 *
 * https://leetcode-cn.com/problems/subsets/description/
 *
 * algorithms
 * Medium (79.23%)
 * Likes:    886
 * Dislikes: 0
 * Total Accepted:    171.4K
 * Total Submissions: 216.4K
 * Testcase Example:  '[1,2,3]'
 *
 * 给定一组不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。
 * 
 * 说明：解集不能包含重复的子集。
 * 
 * 示例:
 * 
 * 输入: nums = [1,2,3]
 * 输出:
 * [
 * ⁠ [3],
 * [1],
 * [2],
 * [1,2,3],
 * [1,3],
 * [2,3],
 * [1,2],
 * []
 * ]
 * 
 */

// @lc code=start
func subsets(nums []int) [][]int {
	res := make([][]int, 0)
	var helper func([]int, int)
	helper = func(path []int, index int) {
		//fmt.Println("path", path)
		tmp := make([]int, len(path))
		copy(tmp, path)
		res = append(res, tmp)
		for i := index; i < len(nums); i++ {
			path = append(path, nums[i])
			helper(path, i + 1)
			path = path[:len(path) - 1]
		}
	}
	path := make([]int, 0, len(nums))
	helper(path, 0)
	return res
}
// @lc code=end

