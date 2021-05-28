func totalHammingDistance(nums []int) int {
	res := 0
	n := len(nums)
	for i := 0; i < 30; i++ {
		c := 0
		// 统计第i位有几个1
		for _, val := range nums {
			if (val>>i)&0x1 == 1 {
				c++
			}
		}
		res += c * (n - c)
	}
	return res
}
