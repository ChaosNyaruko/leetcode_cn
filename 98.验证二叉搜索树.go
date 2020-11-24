import "math"

/*
 * @lc app=leetcode.cn id=98 lang=golang
 *
 * [98] 验证二叉搜索树
 */

// @lc code=start
/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func isValidBST(root *TreeNode) bool {
	prev := math.MinInt64
	var helper func(*TreeNode) bool
	helper = func(r *TreeNode) bool {
		if r == nil {
			return true
		}
		if !helper(r.Left) {
			return false
		}
		if r.Val <= prev {
			return false
		}
		prev = r.Val
		return helper(r.Right)
	}
	return helper(root)
}

// @lc code=end

