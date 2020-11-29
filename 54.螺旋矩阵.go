/*
 * @lc app=leetcode.cn id=54 lang=golang
 *
 * [54] 螺旋矩阵
 *
 * https://leetcode-cn.com/problems/spiral-matrix/description/
 *
 * algorithms
 * Medium (41.61%)
 * Likes:    552
 * Dislikes: 0
 * Total Accepted:    91.8K
 * Total Submissions: 220.7K
 * Testcase Example:  '[[1,2,3],[4,5,6],[7,8,9]]'
 *
 * 给定一个包含 m x n 个元素的矩阵（m 行, n 列），请按照顺时针螺旋顺序，返回矩阵中的所有元素。
 * 
 * 示例 1:
 * 
 * 输入:
 * [
 * ⁠[ 1, 2, 3 ],
 * ⁠[ 4, 5, 6 ],
 * ⁠[ 7, 8, 9 ]
 * ]
 * 输出: [1,2,3,6,9,8,7,4,5]
 * 
 * 
 * 示例 2:
 * 
 * 输入:
 * [
 * ⁠ [1, 2, 3, 4],
 * ⁠ [5, 6, 7, 8],
 * ⁠ [9,10,11,12]
 * ]
 * 输出: [1,2,3,4,8,12,11,10,9,5,6,7]
 * 
 * 
 */

// @lc code=start
func spiralOrder(matrix [][]int) []int {
	m := len(matrix) 
	if m == 0 {
		return nil
	}
	n := len(matrix[0])
	if n == 0 {
		return nil
	}
	res := make([]int, 0, m * n)
	row, col := 0, -1
	for {
		for i := 0; i < n; i++ {
			col++
			res = append(res, matrix[row][col])
		}
		m--
		if m == 0 {
			break
		}
		for i := 0; i < m; i++ {
			row++
			res = append(res, matrix[row][col])
		}
		n--
		if n == 0 {
			break
		}
		for i := 0; i < n; i++ {
			col--
			res = append(res, matrix[row][col])
		}
		m--
		if m == 0 {
			break
		}
		for i := 0 ; i < m; i++ {
			row--
			res = append(res, matrix[row][col])
		}
		n--
		if n == 0 {
			break
		}
	}
	return res
}
// @lc code=end

