func strToInt(str string) int {
	str = strings.TrimSpace(str)
	sign := 1
	res := 0
	for i, c := range str {
		if c >= '0' && c <= '9' {
			res = 10*res + int(c-'0')
		} else if i == 0 && c == '+' {
			sign = 1
		} else if i == 0 && c == '-' {
			sign = -1
		} else {
			break
		}
		if res > math.MaxInt32 {
			if sign == 1 {
				return math.MaxInt32
			}
			return math.MinInt32
		}
	}
	return sign * res
}