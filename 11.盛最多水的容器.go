/*
 * @lc app=leetcode.cn id=11 lang=golang
 *
 * [11] 盛最多水的容器
 */

// @lc code=start
func maxArea(height []int) int {
	if len(height) < 2 {
		return 0
	}
	n := len(height)
	l := 0
	r := n - 1
	res := 0
	for l < r {
		h, lSmaller := min(height[l], height[r])
		cur := (r - l) * h
		res, _ = max(cur, res)
		if !lSmaller { // 由于容积由最小的那块挡板决定，想要获得更大的容积要把小的那块往里挪以期获得更大的结果
			r--
		} else { // 两块挡板一样高的话应该哪块往里移都可以
			l++
		}
	}
	return res
}

func min(a, b int) (int, bool) {
	if a > b {
		return b, false
	}
	return a, true
}

func max(a, b int) (int, bool) {
	if a < b {
		return b, false
	}
	return a, true
}

// @lc code=end

