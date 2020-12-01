// 10->12
func nthUglyNumber(n int) int {
	if n == 0 {
		return 0
	}
	uglyNumbers := make([]int, n)
	uglyNumbers[0] = 1
	p2 := 0
	p3 := 0
	p5 := 0
	for i := 1; i < n; i++ {
		uglyNumbers[i] = min(uglyNumbers[p2]*2, uglyNumbers[p3]*3, uglyNumbers[p5]*5)
		// fmt.Println(uglyNumbers[i])
		if uglyNumbers[i] == (2 * uglyNumbers[p2]) {
			p2++
		}
		if uglyNumbers[i] == (3 * uglyNumbers[p3]) {
			p3++
		}
		if uglyNumbers[i] == (5 * uglyNumbers[p5]) {
			p5++
		}
	}
	return uglyNumbers[n-1]
}

func min(a, b, c int) int {
	m := a
	if b < m {
		m = b
	}
	if c < m {
		m = c
	}
	return m
} 