func countBits(num int) []int {
	res := make([]int, num+1)
	res[0] = 0
	for i := 1; i <= num; i++ {
		res[i] = res[i&(i-1)] + 1
	}
	return res
}
