/*
 * @lc app=leetcode.cn id=46 lang=golang
 *
 * [46] 全排列
 */

// @lc code=start
func helper(start int, nums []int, path []int, res *[][]int) {
	if start == len(nums) {
		copyPath := make([]int, len(path))
		copy(copyPath, path)
		*res = append(*res, copyPath)
		return
	}
	for i := start; i < len(nums); i++ {
		// *path = append(*path, nums[start])
		path[start], path[i] = path[i], path[start]
		helper(start+1, nums, path, res)
		// *path = (*path)[:len(*path)-1]
		path[start], path[i] = path[i], path[start]
	}
	return
}

func permute(nums []int) [][]int {
	res := make([][]int, 0)
	path := make([]int, len(nums))
	copy(path, nums)
	helper(0, nums, path, &res)
	return res
}

// @lc code=end

