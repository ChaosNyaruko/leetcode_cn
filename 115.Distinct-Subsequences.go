func numDistinct(s string, t string) int {
	m, n := len(s), len(t)
	if m < n {
		return 0
	}
	dp := make([][]int, m+1)
	for i := 0; i < m+1; i++ {
		dp[i] = make([]int, n+1)
	}
	for i := 0; i < m+1; i++ {
		dp[i][0] = 1
	}
	for j := 1; j < n+1; j++ {
		dp[0][j] = 0
	}
	for j := 0; j < n; j++ {
		for i := 0; i < m; i++ {
			if s[i] == t[j] {
				dp[i+1][j+1] = dp[i][j+1] + dp[i][j]
			} else {
				dp[i+1][j+1] = dp[i][j+1]
			}
		}
	}
	return dp[m][n]
}
