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