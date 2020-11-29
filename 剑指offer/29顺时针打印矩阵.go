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
