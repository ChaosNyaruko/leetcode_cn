func constructArr(a []int) []int {
	if len(a) == 0 {
		return []int{}
	}
	res := make([]int, len(a))
	cur := 1
	res[0] = 1
	for i := 1; i < len(a); i++ {
		cur *= a[i-1]
		res[i] = cur
	}
	cur = 1
	for i := len(a) - 2; i >= 0; i-- {
		cur *= a[i+1]
		res[i] = res[i] * cur
	}
	return res
}