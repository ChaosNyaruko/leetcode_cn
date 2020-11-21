/*
 * @lc app=leetcode.cn id=79 lang=golang
 *
 * [79] 单词搜索
 *
 * https://leetcode-cn.com/problems/word-search/description/
 *
 * algorithms
 * Medium (43.75%)
 * Likes:    685
 * Dislikes: 0
 * Total Accepted:    120.9K
 * Total Submissions: 276.2K
 * Testcase Example:  '[["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]\n"ABCCED"'
 *
 * 给定一个二维网格和一个单词，找出该单词是否存在于网格中。
 * 
 * 单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。
 * 
 * 
 * 
 * 示例:
 * 
 * board =
 * [
 * ⁠ ['A','B','C','E'],
 * ⁠ ['S','F','C','S'],
 * ⁠ ['A','D','E','E']
 * ]
 * 
 * 给定 word = "ABCCED", 返回 true
 * 给定 word = "SEE", 返回 true
 * 给定 word = "ABCB", 返回 false
 * 
 * 
 * 
 * 提示：
 * 
 * 
 * board 和 word 中只包含大写和小写英文字母。
 * 1 <= board.length <= 200
 * 1 <= board[i].length <= 200
 * 1 <= word.length <= 10^3
 * 
 * 
 */

// @lc code=start
func exist(board [][]byte, word string) bool {
	m := len(board)
	n := len(board[0])
	if m == 0 || n == 0 {
		return false
	}
	visited := make([][]bool, m)
	for i := 0; i < m; i++ {
		visited[i] = make([]bool ,n)
	}
	var helper func(int, int, int) bool
	helper = func(x,y int, index int) bool {
		if x >= m || x < 0 || y >= n || y < 0 || visited[x][y] {
			return false
		}
		if index == len(word) - 1 {
			return word[index] == board[x][y]
		}
		if board[x][y] != word[index] {
			return false
		}
		visited[x][y] = true
		if helper(x + 1, y, index + 1) {
			visited[x][y] = false
			return true
		}
		if helper(x - 1, y, index + 1) {
			visited[x][y] = false
			return true
		}
		if helper(x, y + 1, index + 1) {
			visited[x][y] = false
			return true
		}
		if helper(x, y - 1, index + 1) {
			visited[x][y] = false
			return true
		}
		visited[x][y] = false
		return false
	}
	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			if board[i][j] == word[0] {
				if helper(i, j, 0) {
					return true
				}
			}
		}
	}
	return false
}
// @lc code=end

