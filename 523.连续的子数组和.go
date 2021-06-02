func checkSubarraySum(nums []int, k int) bool {
	n := len(nums)
	sum := make([]int, n+1)
	for i := 1; i < n+1; i++ {
		sum[i] = sum[i-1] + nums[i-1]
	}
	m := make(map[int]int)
	for i, s := range sum {
		r := s % k
		if early, ok := m[r]; ok {
			if i-early >= 2 {
				return true
			}
		} else {
			m[r] = i
		}
	}
	return false
}
