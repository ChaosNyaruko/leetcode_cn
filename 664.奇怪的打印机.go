import "math"

func strangePrinter(s string) int {
	n := len(s)
	// dp[i][j]表示打印出s[i..j]的最少打印次数
	dp := make([][]int, n)
	for i := 0; i < n; i++ {
		dp[i] = make([]int, n)
	}

	for i := 0; i < n; i++ {
		dp[i][i] = 1
	}

	for l := 2; l <= n; l++ {
		for i := 0; i < n-l+1; i++ {
			j := i + l - 1
			if s[i] == s[j] {
				dp[i][j] = dp[i][j-1]
			} else {
				minn := math.MaxInt32
				for k := i; k < j; k++ {
					minn = min(minn, dp[i][k]+dp[k+1][j])
				}
				dp[i][j] = minn
			}
		}
	}

	return dp[0][n-1]
}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}
