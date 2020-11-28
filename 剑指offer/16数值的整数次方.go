func helper(x float64, n uint) float64 {
    if n == 0 {
        return 1
    }
    if n == 1 {
        return x
    }
    result := helper(x, n >> 1)
    result *= result
    if n & 1 == 1 {
        result *= x
    }
    return result
}
func myPow(x float64, n int) float64 {
    if x == 0  && n < 0{
        return 0.0
    }
    un := uint(n)
    if n < 0 {
        un = uint(-n)
    }

    res := helper(x, un)
    if n < 0 {
        return 1.0/res
    }
    return res
}