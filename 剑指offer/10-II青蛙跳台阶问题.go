func numWays(n int) int {
    if n == 0 {
        return 1
    }
    if n == 1 {
        return 1
    }
    f1, f2 := 1, 1
    for i := 2; i <= n; i++ {
        f1, f2 = (f1 + f2) % (1e9+7), f1
    }
    return f1
}