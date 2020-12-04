func maxProfit(prices []int) int {
	if len(prices) == 0 {
		return 0
	}
	// dp[i] 第i天卖出（买入肯定在i-1及之前)
	curMin := prices[0]
	maxSellingAtI := 0
	res := 0
	for i := 1; i < len(prices); i++ {
		maxSellingAtI = prices[i] - curMin
		curMin = min(curMin, prices[i])
		res = max(res, maxSellingAtI)
	}
	return res
}
func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}
func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}