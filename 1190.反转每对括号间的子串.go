func reverseParentheses(s string) string {
	pair := make([]int, len(s))
	stk := make([]int, 0)
	for i, c := range s {
		if c == '(' {
			stk = append(stk, i)
		} else if c == ')' {
			left := stk[len(stk)-1]
			stk = stk[:len(stk)-1]
			pair[left] = i
			pair[i] = left
		}
	}
	index, dir := 0, 1
	res := make([]byte, 0)
	for index < len(s) {
		if s[index] == '(' || s[index] == ')' {
			index = pair[index]
			dir = -dir
		} else {
			res = append(res, s[index])
		}
		index += dir
	}
	return string(res)
}
