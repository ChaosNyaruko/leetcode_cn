/*
 * @lc app=leetcode.cn id=85 lang=golang
 *
 * [85] 最大矩形
 */

// @lc code=start
func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

func maximalRectangle(matrix [][]byte) int {
	m := len(matrix)
	if m == 0 {
		return 0
	}
	n := len(matrix[0])
	if n == 0 {
		return 0
	}

	left := make([]int, n)
	right := make([]int, n)
	for k := 0; k < n; k++ {
		right[k] = n
	}
	res := 0
	heights := make([]int, n)
	for i := 0; i < m; i++ {
		curLeft := 0
		for j := 0; j < n; j++ {
			if matrix[i][j] == '1' {
				heights[j]++
				left[j] = max(left[j], curLeft)
			} else {
				heights[j] = 0
				left[j] = 0 //
				curLeft = j + 1
			}
		}

		//fmt.Println("left:", left)
		curRight := n
		for j := n - 1; j >= 0; j-- {
			if matrix[i][j] == '1' {
				right[j] = min(right[j], curRight)
			} else {
				right[j] = n //
				curRight = j
			}
		}
		//fmt.Println("right", right)

		//fmt.Println("height", heights)
		for j := 0; j < n; j++ {
			res = max(res, heights[j]*(right[j]-left[j]))
		}
	}
	return res
}

// @lc code=end

