func dicesProbability(n int) []float64 {
	var dp [2][]int
	dp[0] = make([]int, 6*11+1)
	dp[1] = make([]int, 6*11+1)
	// dp[i][j]表示抛了i个骰子后和为j的次数
	// dp[i][j] = sum(dp[i-1][j - k]) (k = 1~6)
	for j := 1; j <= 6; j++ {
		dp[0][j] = 1
	}
	current := 0
	for i := 2; i <= n; i++ {
		//fmt.Println("i=", i, "dp=", dp[current], "current:", current)
		current = 1 - current
		for j := i; j <= 6*i; j++ {
			dp[current][j] = 0
			for k := 1; k <= 6; k++ {
				if j-k >= i-1 {
					dp[current][j] += dp[1-current][j-k]
				}
			}
		}
	}
	//fmt.Println("final", "current=", current, dp[current])
	all := math.Pow(6, float64(n))
	res := make([]float64, 0)
	for i := n; i <= 6*n; i++ {
		res = append(res, float64(dp[current][i])/all)
	}
	return res
}