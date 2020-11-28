/*
 * @lc app=leetcode.cn id=50 lang=golang
 *
 * [50] Pow(x, n)
 *
 * https://leetcode-cn.com/problems/powx-n/description/
 *
 * algorithms
 * Medium (36.95%)
 * Likes:    550
 * Dislikes: 0
 * Total Accepted:    141.3K
 * Total Submissions: 382.4K
 * Testcase Example:  '2.00000\n10'
 *
 * 实现 pow(x, n) ，即计算 x 的 n 次幂函数。
 * 
 * 示例 1:
 * 
 * 输入: 2.00000, 10
 * 输出: 1024.00000
 * 
 * 
 * 示例 2:
 * 
 * 输入: 2.10000, 3
 * 输出: 9.26100
 * 
 * 
 * 示例 3:
 * 
 * 输入: 2.00000, -2
 * 输出: 0.25000
 * 解释: 2^-2 = 1/2^2 = 1/4 = 0.25
 * 
 * 说明:
 * 
 * 
 * -100.0 < x < 100.0
 * n 是 32 位有符号整数，其数值范围是 [−2^31, 2^31 − 1] 。
 * 
 * 
 */

// @lc code=start
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
// @lc code=end

