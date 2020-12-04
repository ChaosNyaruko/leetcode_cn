func isStraight(nums []int) bool {
	m := make(map[int]struct{})
	mx, mn := 0, 14
	for _, num := range nums {
		if num == 0 {
			continue
		}
		if _, ok := m[num]; ok {
			return false
		}
		mx = max(mx, num)
		mn = min(mn, num)
		m[num] = struct{}{}
	}
	return mx-mn < 5
}
func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}