func singleNumber(nums []int) int {
	// ones的第[i]位为1表示遍历到当前为止的数第i位有3k+1个是1
	ones := 0
	twos := 0
	threes := 0
	for _, num := range nums {
		twos |= ones & num
		ones = ones ^ num
		threes = twos & ones
		twos &= ^threes
		ones &= ^threes
	}
	return ones
}