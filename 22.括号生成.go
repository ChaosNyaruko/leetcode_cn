/*
 * @lc app=leetcode.cn id=22 lang=golang
 *
 * [22] 括号生成
 *
 * https://leetcode-cn.com/problems/generate-parentheses/description/
 *
 * algorithms
 * Medium (76.46%)
 * Likes:    1402
 * Dislikes: 0
 * Total Accepted:    196K
 * Total Submissions: 256.4K
 * Testcase Example:  '3'
 *
 * 数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。
 * 
 * 
 * 
 * 示例：
 * 
 * 输入：n = 3
 * 输出：[
 * ⁠      "((()))",
 * ⁠      "(()())",
 * ⁠      "(())()",
 * ⁠      "()(())",
 * ⁠      "()()()"
 * ⁠    ]
 * 
 * 
 */

 
// @lc code=start
func helper(open, close, n int, path string, res *[]string) {
	 if open == n && close == n {
		 *res = append(*res, path)
		 return
	 }
	 if open < n {
		 helper(open + 1, close, n, path + "(", res)
	 }
	 if close < open {
		 helper(open, close + 1, n, path + ")", res)
	 }
	 return 
 }
func generateParenthesis(n int) []string {
	path := ""
	res := make([]string, 0)
	p := &res
	helper(0, 0, n, path, p)
	return *p
}
// @lc code=end

