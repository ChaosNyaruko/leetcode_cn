func evalRPN(tokens []string) int {
    stk := make([]int, 0)
    for _, token := range tokens {
        switch token {
        case "+":
            a, b := stk[len(stk) - 1], stk[len(stk) - 2]
            stk = stk[:len(stk) - 2]
            stk = append(stk, a + b)
        case "-":
            a, b := stk[len(stk) - 1], stk[len(stk) - 2]
            stk = stk[:len(stk) - 2]
            stk = append(stk, b - a)
        case "*":
            a, b := stk[len(stk) - 1], stk[len(stk) - 2]
            stk = stk[:len(stk) - 2]
            stk = append(stk, a * b)
        case "/":
            a, b := stk[len(stk) - 1], stk[len(stk) - 2]
            stk = stk[:len(stk) - 2]
            stk = append(stk, b / a)
        default:
            val, _ := strconv.Atoi(token)
            stk = append(stk, val)
        }
    }
    return stk[len(stk) - 1]
}
