func sumNums(n int) int {
	res := 0
	var helper func(int) bool
	helper = func(n int) bool {
		res += n
		return n > 0 && helper(n-1)
	}
	helper(n)
	return res
}