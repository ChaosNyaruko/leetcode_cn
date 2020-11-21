/*
 * @lc app=leetcode.cn id=76 lang=golang
 *
 * [76] 最小覆盖子串
 *
 * https://leetcode-cn.com/problems/minimum-window-substring/description/
 *
 * algorithms
 * Hard (39.67%)
 * Likes:    835
 * Dislikes: 0
 * Total Accepted:    89.6K
 * Total Submissions: 226K
 * Testcase Example:  '"ADOBECODEBANC"\n"ABC"'
 *
 * 给你一个字符串 s 、一个字符串 t 。返回 s 中涵盖 t 所有字符的最小子串。如果 s 中不存在涵盖 t 所有字符的子串，则返回空字符串 "" 。
 * 
 * 注意：如果 s 中存在这样的子串，我们保证它是唯一的答案。
 * 
 * 
 * 
 * 示例 1：
 * 
 * 
 * 输入：s = "ADOBECODEBANC", t = "ABC"
 * 输出："BANC"
 * 
 * 
 * 示例 2：
 * 
 * 
 * 输入：s = "a", t = "a"
 * 输出："a"
 * 
 * 
 * 
 * 
 * 提示：
 * 
 * 
 * 1 
 * s 和 t 由英文字母组成
 * 
 * 
 * 
 * 进阶：你能设计一个在 o(n) 时间内解决此问题的算法吗？
 */

// @lc code=start
func minWindow(s string, t string) string {
	cnt := make([]int, 256)
	for _, c := range t {
		cnt[c]++
	}
	match := len(t)
	l, r := 0, 0
	d := math.MaxInt32
	resL := 0
	for r < len(s) {
		if cnt[s[r]] > 0 {
			match--
		}
		cnt[s[r]]--
		for match == 0 {
			cnt[s[l]]++
			if cnt[s[l]] > 0 {
				match++
			}
			if r - l + 1 < d {
				d = r - l + 1
				resL = l
			}
			l++
		}
		r++
	}
	if d == math.MaxInt32 {
		return ""
	}
	return s[resL:resL+d]
}
// @lc code=end

