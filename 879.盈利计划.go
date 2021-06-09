func profitableSchemes(n int, minProfit int, group []int, profit []int) int {
	m := len(group)
	dp := make([][][]int, m+1)
	for i := 0; i <= m; i++ {
		dp[i] = make([][]int, n+1)
		for j := 0; j <= n; j++ {
			dp[i][j] = make([]int, minProfit+1)
		}
	}
	MOD := int(1e9 + 7)
	dp[0][0][0] = 1
	for i := 1; i <= m; i++ {
		for j := 0; j <= n; j++ {
			for k := 0; k <= minProfit; k++ {
				if j < group[i-1] {
					dp[i][j][k] = dp[i-1][j][k]
				} else {
					dp[i][j][k] = (dp[i-1][j][k] + dp[i-1][j-group[i-1]][max(0, k-profit[i-1])]) % MOD
				}
			}
		}
	}
	res := 0
	for i := 0; i <= n; i++ {
		res = (res + dp[m][i][minProfit]) % MOD
	}
	return res
}
