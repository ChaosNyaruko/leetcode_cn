// 简单易理解的动态规划解法，不考虑空间优化
func translateNum_1(num int) int {
    if num == 0 {
        return 1
    }
    // dp[i]表示以nums[i-1]为结尾时的翻译方法数
    str := strconv.Itoa(num)
    if len(str) == 1 {
        return 1
    }
    dp := make([]int, len(str)+1)
    dp[0] = 1
    dp[1] = 1
    for i := 2; i <= len(str); i++ {
        dp[i] = dp[i-1]
        if str[i-2] =='1' && str[i-1] >= '0' && str[i-1] <= '9' {
            dp[i] += dp[i-2]
        }
        if str[i-2] == '2' && str[i-1] >= '0' && str[i-1] <= '5' {
            dp[i] += dp[i-2]
        }
    }
    return dp[len(str)]
}

// 简洁的递归解法
func translateNum(num int) int {
    if num == 0 {
        return 1
    }
    if num % 100 <= 25 && num % 100 >= 10 {
        return translateNum(num/100) + translateNum(num/10)
    } else {
        return translateNum(num/10)
    }
}

