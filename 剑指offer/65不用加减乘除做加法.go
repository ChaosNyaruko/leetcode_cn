func add(a int, b int) int {
	sum := a
	carry := b
	for carry != 0 {
		nextCarry := (sum & carry) << 1
		sum = sum ^ carry
		carry = nextCarry
	}
	return sum
}