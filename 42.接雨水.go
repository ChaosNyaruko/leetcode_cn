/*
 * @lc app=leetcode.cn id=42 lang=golang
 *
 * [42] 接雨水
 */

// @lc code=start
func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

func trap(height []int) int {
	res := 0
	i := 0
	stk := []int{}
	for i < len(height) {
		h := height[i]
		if len(stk) == 0 || h <= height[stk[len(stk)-1]] {
			stk = append(stk, i)
			i++
		} else {
			popi := stk[len(stk)-1]
			stk = stk[:len(stk)-1] // pop()
			if len(stk) > 0 {
				topi := stk[len(stk)-1]
				top := height[topi]
				res += (min(top, h) - height[popi]) * (i - topi - 1)
			}
		}
	}
	return res
}

// @lc code=end

