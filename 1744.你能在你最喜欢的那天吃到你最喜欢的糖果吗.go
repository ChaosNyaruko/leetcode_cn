func canEat(candiesCount []int, queries [][]int) []bool {
	sum := make([]int, len(candiesCount))
	sum[0] = candiesCount[0]
	for i := 1; i < len(candiesCount); i++ {
		sum[i] = sum[i-1] + candiesCount[i]
	}

	res := make([]bool, len(queries))
	for i, q := range queries {
		x1, y1 := q[1]+1, (q[1]+1)*q[2]
		x2 := 1
		if q[0] > 0 {
			x2 = sum[q[0]-1] + 1
		}
		y2 := sum[q[0]]
		res[i] = !((y1 < x2) || (y2 < x1))
	}
	return res
}
