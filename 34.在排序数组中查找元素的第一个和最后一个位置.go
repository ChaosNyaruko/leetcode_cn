/*
 * @lc app=leetcode.cn id=34 lang=golang
 *
 * [34] 在排序数组中查找元素的第一个和最后一个位置
 */

// @lc code=start
func searchRange(nums []int, target int) []int {
	n := len(nums)
	l := 0
	r := n - 1
	for l < r {
		m := l + (r-l)/2
		if nums[m] < target {
			l = m + 1
		} else {
			r = m
		}
	}
	if l >= len(nums) || nums[l] != target {
		return []int{-1, -1}
	}
	res1 := l
	r = n - 1
	for l < r {
		m := l + (r-l+1)/2 // 找右边界
		// fmt.Println(l, m, r, nums[l], nums[m], nums[r])
		if nums[m] > target {
			r = m - 1
		} else {
			l = m
		}
	}
	res2 := r
	return []int{res1, res2}
}

// @lc code=end
// [5,7,7,8,8,10] 8
