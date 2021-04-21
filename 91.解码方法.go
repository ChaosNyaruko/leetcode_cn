func numDecodings(s string) int {
	dp := make([]int, len(s)+1)
	// dp[i] = dp[i - 1] (s[i - 1] != 0 ) + dp[i - 2](s[i-2]*10+s[i-1] >= 10 <= 26)
	dp[0] = 1
	for i := 1; i <= len(s); i++ {
		if s[i-1] != '0' {
			dp[i] = dp[i-1]
		}
		if i >= 2 {
			a, b := s[i-2]-'0', s[i-1]-'0'
			c := 10*a + b
			if c >= 10 && c <= 26 {
				dp[i] += dp[i-2]
			}
		}
	}
	return dp[len(s)]
}
