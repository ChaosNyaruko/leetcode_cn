/*
 * @lc app=leetcode.cn id=5 lang=golang
 *
 * [5] 最长回文子串
 */

// @lc code=start
func longestPalindrome(s string) string {
	n := len(s)
	if n == 0 {
		return ""
	}
	lo := 0
	d := 0
	dp := [1000][1000]bool{} // 懒得写初始化了

	for i := 0; i < n; i++ {
		for j := 0; j <= i; j++ {
			if i-j <= 2 {
				dp[j][i] = s[i] == s[j]
			} else {
				dp[j][i] = dp[j+1][i-1] && (s[i] == s[j])
			}
			if dp[j][i] && i-j+1 > d {
				lo = j
				d = i - j + 1
			}
		}
	}
	return s[lo : lo+d]
}

// @lc code=end

