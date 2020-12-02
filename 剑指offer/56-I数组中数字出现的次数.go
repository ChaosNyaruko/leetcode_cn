func singleNumbers(nums []int) []int {
	xor := 0
	for _, num := range nums {
		xor = xor ^ num
	}
	// fmt.Println(xor)
	xor = xor & (-xor)
	// fmt.Println(xor)
	a := 0
	b := 0
	for _, num := range nums {
		if num&xor != 0 {
			a = a ^ num
		} else {
			b = b ^ num
		}
	}
	return []int{a, b}
}