func calculate(s string) int {
	stk := []int{}
	num := 0
	sign := '+'
	for i, ch := range s {
		isDigit := ch >= '0' && ch <= '9'
		if isDigit {
			num = 10*num + int(ch-'0')
		}
		if !isDigit && ch != ' ' || i == len(s)-1 {
			switch sign {
			case '+':
				stk = append(stk, num)
			case '-':
				stk = append(stk, -num)
			case '*':
				stk[len(stk)-1] *= num
			case '/':
				stk[len(stk)-1] /= num
			}
			num = 0
			sign = ch
		}
	}
	res := 0
	for _, v := range stk {
		res += v
	}
	return res
}
