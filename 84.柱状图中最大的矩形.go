/*
 * @lc app=leetcode.cn id=84 lang=golang
 *
 * [84] 柱状图中最大的矩形
 */

// @lc code=start
func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func largestRectangleArea(heights []int) int {
	heights = append(heights, 0)
	stk := make([]int, 0, len(heights))
	res := 0
	for i := 0; i < len(heights); i++ {
		//fmt.Println("*****", i, heights[i], "stk:", stk, "len(stk):", len(stk))
		for len(stk) != 0 && heights[stk[len(stk)-1]] >= heights[i] {
			hi := stk[len(stk)-1]
			h := heights[hi]
			stk = stk[:len(stk)-1]
			width := 0
			if len(stk) == 0 {
				width = i
			} else {
				width = i - stk[len(stk)-1] - 1
			}
			//fmt.Println("i=", i, "heights[i]=", heights[i], "res=", res, "cur", width*h)
			res = max(res, width*h)
		}
		stk = append(stk, i)
		//fmt.Println("after pushing i", i, stk)
	}
	return res
}

// @lc code=end

