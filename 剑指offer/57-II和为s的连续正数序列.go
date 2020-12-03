func findContinuousSequence(target int) [][]int {
	l, r := 1, 2
	res := make([][]int, 0)
	sum := l + r
	path := []int{l, r}
	for l < r {
		if sum == target {
			tmp := make([]int, len(path))
			copy(tmp, path)
			res = append(res, tmp)
			sum -= l
			l++ // r++
			path = path[1:]
		} else if sum < target {
			r++
			sum += r
			path = append(path, r)
		} else {
			sum -= l
			l++
			path = path[1:]
		}
	}
	return res
}