/*
 * @lc app=leetcode.cn id=32 lang=golang
 *
 * [32] 最长有效括号
 *
 * https://leetcode-cn.com/problems/longest-valid-parentheses/description/
 *
 * algorithms
 * Hard (34.02%)
 * Likes:    1055
 * Dislikes: 0
 * Total Accepted:    110.4K
 * Total Submissions: 324.3K
 * Testcase Example:  '"(()"'
 *
 * 给定一个只包含 '(' 和 ')' 的字符串，找出最长的包含有效括号的子串的长度。
 * 
 * 示例 1:
 * 
 * 输入: "(()"
 * 输出: 2
 * 解释: 最长有效括号子串为 "()"
 * 
 * 
 * 示例 2:
 * 
 * 输入: ")()())"
 * 输出: 4
 * 解释: 最长有效括号子串为 "()()"
 * 
 * 
 */

// @lc code=start
func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}
// stack 100% 33.14%
func longestValidParentheses_stack(s string) int {
	stk := []int{-1}
	res := 0
	for i, c := range s {
		if c == '(' {
			stk = append(stk, i)
		} else {
			stk = stk[:len(stk) -1]
			if len(stk) == 0 {
				stk = append(stk, i)
			} else {
				res = max(res, i - stk[len(stk)-1])		
			}
		}
	}
	return res
}
// counter 100% 96.4%
func longestValidParentheses_counter(s string) int {
	left := 0
	right := 0
	res := 0
	for _, c := range s {
		if c == '(' {
			left++
		} else {
			right++
		}
		if left == right {
			res = max(res, left + right)
		} else if left < right {
			left, right = 0, 0
		}
	}
	left, right = 0, 0
	for i := len(s) - 1; i>=0; i-- {
		if s[i] == ')' {
			right++ 
		} else {
			left++
		}
		if left == right {
			res = max(res, left + right)
		} else if left > right{
			left, right =0, 0
		}
	}
	return res
} 
// dp 100% 61.17%
func longestValidParentheses(s string) int {
	// dp[i]表示以s[i]结尾的最长有效括号的长度
	dp := make([]int, len(s))
	res := 0
	for i := 1; i < len(s); i++ {
		// 只有以)结尾的才有可能是有效括号
		if  s[i] == ')' {
			if s[i - 1] == '(' {
				dp[i] += 2
				if i >= 2 {
					dp[i] += dp[i - 2]
				}
			} else { // s[i-1] == ')'
				if i - 1 - dp[i-1] >= 0 && s[i -1 - dp[i-1]] == '(' {
					dp[i] = dp[i-1] + 2 
					if i - 1 -dp[i-1] - 1 >= 0 {
						dp[i] += dp[i-1-dp[i-1]-1]
					}
				}
			}
		}
		res = max(res, dp[i])
	}
	return res
}

// @lc code=end

