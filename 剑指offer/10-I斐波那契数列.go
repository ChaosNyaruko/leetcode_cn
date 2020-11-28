func fib(n int) int {
    if n == 0 {
        return 0
    }
    if n == 1 {
        return 1
    }
    f1, f2 := 1, 0
    for i := 2; i <= n; i++ {
        f1, f2 = (f1 + f2) % (1e9+7), f1
    }
    return f1
}