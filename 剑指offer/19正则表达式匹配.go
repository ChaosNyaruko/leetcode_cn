func isMatch(s string, p string) bool {
	m, n := len(s), len(p)
	dp := make([][]bool, m+1)
	for i := range dp {
		dp[i] = make([]bool, n+1)
	}
	// dp[i][j]表示s[0..i-1]p[0..j-1] 是否匹配
	dp[0][0] = true
	for i := 0; i <= m; i++ {
		// dp[i][0] 在i!=0 时肯定是false，匹配不上
		for j := 1; j <= n; j++ {
			if p[j-1] == '*' && j >= 2 {
				dp[i][j] = dp[i][j-2] /* 匹配0个*/ || i > 0 && dp[i-1][j] && (s[i-1] == p[j-2] || p[j-2] == '.') /* 匹配至少一个*/
			} else {
				dp[i][j] = i > 0 && dp[i-1][j-1] && (s[i-1] == p[j-1] || p[j-1] == '.')
			}
		}
	}
	return dp[m][n]
}