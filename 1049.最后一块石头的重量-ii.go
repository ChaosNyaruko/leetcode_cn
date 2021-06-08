func lastStoneWeightII(stones []int) int {
	sum := 0
	for _, stone := range stones {
		sum += stone
	}

	// sum - n - n >= 0
	// ---> n <= sum / 2
	target := sum / 2
	dp := make([][]bool, len(stones)+1)
	for i := 0; i <= len(stones); i++ {
		dp[i] = make([]bool, target+1)
	}
	dp[0][0] = true
	for i := 1; i <= len(stones); i++ {
		for j := 0; j <= target; j++ {
			if j < stones[i-1] {
				dp[i][j] = dp[i-1][j]
			} else {
				dp[i][j] = dp[i-1][j] || dp[i-1][j-stones[i-1]]
			}
		}
	}
	for j := target; j >= 0; j-- {
		if dp[len(stones)][j] {
			return sum - 2*j
		}
	}
	return 0
}
