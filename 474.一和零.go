func findMaxForm(strs []string, m int, n int) int {
	l := len(strs)
	dp := make([][][]int, l+1)
	for i := 0; i <= l; i++ {
		dp[i] = make([][]int, m+1)
		for j := 0; j <= m; j++ {
			dp[i][j] = make([]int, n+1)
		}
	}
	for i := 1; i <= l; i++ {
		str := strs[i-1]
		zeros, ones := getZerosOne(str)
		for j := 0; j <= m; j++ {
			for k := 0; k <= n; k++ {
				if zeros > j || ones > k {
					dp[i][j][k] = dp[i-1][j][k]
				} else {
					dp[i][j][k] = max(dp[i-1][j-zeros][k-ones]+1, dp[i-1][j][k])
				}
			}
		}
	}
	return dp[l][m][n]
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}
func getZerosOne(str string) (zeros, ones int) {
	for _, c := range str {
		if c == '0' {
			zeros++
		} else {
			ones++
		}
	}
	return
}
