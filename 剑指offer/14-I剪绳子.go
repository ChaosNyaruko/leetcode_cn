func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func cuttingRope(n int) int {
	if n < 2 {
		return 0	
	}
	if n == 2 {
		return 1
	}
	if n == 3 {
		return 2
	}
	// dp[i]表示将整数i 拆分成几个数时（可以为1，即不拆），获得的最大乘积
	dp := make([]int, n + 1)
	dp[0] = 0
	dp[1] = 1
	dp[2] = 2
	dp[3] = 3
	for i := 4; i <=n ; i++ {
		for j := 1; j <= i / 2; j++ {
			dp[i] = max(dp[i], dp[j]*dp[i-j])
		}
	}
	return dp[n]
}