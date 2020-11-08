/*
 * @lc app=leetcode.cn id=33 lang=golang
 *
 * [33] 搜索旋转排序数组
 */

// @lc code=start
func search(nums []int, target int) int {
	n := len(nums)
	// find rotate point
	l := 0
	r := n - 1
	for l < r {
		m := l + (r-l)/2
		// fmt.Println(l, r, m, nums[l], nums[r], nums[m])
		// nums里的数是严格不相等的
		if nums[m] > nums[r] { // 旋转点在右半边
			l = m + 1
		} else { // 旋转点在左半边
			r = m
		}
	}
	rot := l
	// fmt.Print(rot)
	l = 0
	r = n - 1
	for l < r {
		m := l + (r-l)/2
		mm := (m + rot) % n
		if nums[mm] < target {
			l = m + 1
		} else {
			r = m
		}
	}
	if l >= n || nums[(l+rot)%n] != target {
		return -1
	}
	return (l + rot) % n
}

// @lc code=end

