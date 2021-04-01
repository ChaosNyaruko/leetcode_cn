func clumsy(N int) int {
	stk := []int{N}
	N--
	oper := 0
	for N > 0 {
		if oper%4 == 0 {
			top := stk[len(stk)-1]
			stk = stk[:len(stk)-1]
			stk = append(stk, top*N)
		} else if oper%4 == 1 {
			top := stk[len(stk)-1]
			stk = stk[:len(stk)-1]
			stk = append(stk, top/N)
		} else if oper%4 == 2 {
			stk = append(stk, N)
		} else {
			stk = append(stk, -N)
		}
		N--
		oper++
	}
	res := 0
	for _, n := range stk {
		res += n
	}
	return res
}
