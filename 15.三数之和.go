import "sort"

/*
 * @lc app=leetcode.cn id=15 lang=golang
 *
 * [15] 三数之和
 */

// @lc code=start
func threeSum(nums []int) [][]int {
	sort.Ints(nums)
	n := len(nums)
	res := make([][]int, 0, 100)
	for i := 0; i < n-2; i++ {
		if i > 0 && nums[i] == nums[i-1] {
			continue
		}
		a := nums[i]
		target := -a
		l, r := i+1, n-1
		for l < r {
			if l > i+1 && nums[l] == nums[l-1] {
				l++
				continue
			}
			cur := nums[l] + nums[r]
			if cur > target {
				r--
			} else if cur < target {
				l++
			} else {
				res = append(res, []int{nums[i], nums[l], nums[r]})
				l++
				r--
			}
		}
	}
	return res
}

// @lc code=end

