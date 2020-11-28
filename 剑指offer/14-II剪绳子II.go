//不用big，不好做
func cuttingRope(n int) int {
    if n <= 3 {
        return n - 1
    }

    dp := make([]*big.Int, n+1)
    dp[0] =big.NewInt(0)
    dp[1] = big.NewInt(1)
    dp[2] = big.NewInt(2)
    dp[3] = big.NewInt(3)
    for i := 4; i <= n; i++ {
        dp[i] = big.NewInt(0)
        for j := 1; j <= i/2; j++ {
            d := big.NewInt(1)
            //fmt.Println(i,dp[i],dp[j],dp[i-j],11)
            dp[i] = MaxBig(dp[i], d.Mul(dp[j],dp[i-j]))
        }
    }
    //fmt.Println(dp)
    d := dp[n].Mod(dp[n],big.NewInt(1000000007))
    return  int(d.Int64())
}
func MaxBig(a, b *big.Int) *big.Int {
    if a.Cmp(b) > 0 {
    return a
    }
    return b
}
