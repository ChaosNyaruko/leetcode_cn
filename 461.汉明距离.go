func hammingDistance(x int, y int) int {
	s := x ^ y
	cnt := 0
	for s != 0 {
		cnt++
		s = s & (s - 1)
	}
	return cnt
}
