func validateStackSequences(pushed []int, popped []int) bool {
	stk := make([]int, 0, len(pushed))
	p1, p2 := 0, 0
	for p2 < len(popped) {
		for len(stk) == 0 ||  stk[len(stk) - 1] != popped[p2] {
			if p1 < len(pushed) {
				stk = append(stk, pushed[p1])
				p1++
			} else {
				break
			}
		}
		if stk[len(stk) - 1] != popped[p2] {
			return false
		}
		stk = stk[:len(stk) - 1]
		p2++
	}
	return true
}