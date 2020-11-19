import (
	"sort"
)

/*
 * @lc app=leetcode.cn id=47 lang=golang
 *
 * [47] 全排列 II
 */

// @lc code=start
func permuteUnique(nums []int) [][]int {
	sort.Ints(nums)
	res := make([][]int, 0)
	n := len(nums)
	visited := make([]bool, n)
	path := make([]int, 0, n)
	var helper func(int)
	helper = func(idx int) {
		if idx == n {
			tmp := make([]int, len(path))
			copy(tmp, path)
			res = append(res, tmp)
			return
		}

		for i, v := range nums {
			if visited[i] || i > 0 && nums[i] == nums[i-1] && !visited[i-1] {
				continue
			}
			path = append(path, v)
			visited[i] = true
			helper(idx + 1)
			visited[i] = false
			path = path[:len(path)-1]
		}
		return
	}
	helper(0)
	return res
}

// @lc code=end

