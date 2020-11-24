/*
 * @lc app=leetcode.cn id=96 lang=golang
 *
 * [96] 不同的二叉搜索树
 */

// @lc code=start
func numTrees(n int) int {
	if n <= 1 {
		return 1
	}
	f := make([]int, n+1)
	f[0] = 1
	f[1] = 1
	for i := 2; i <= n; i++ {
		for j := 1; j <= i; j++ {
			f[i] += f[j-1] * f[i-j]
		}
	}
	return f[n]
}

// @lc code=end

