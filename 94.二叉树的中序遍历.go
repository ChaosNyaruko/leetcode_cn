/*
 * @lc app=leetcode.cn id=94 lang=golang
 *
 * [94] 二叉树的中序遍历
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
func inorderTraversal(root *TreeNode) []int {
	if root == nil {
		return []int{}
	}
	stk := []*TreeNode{}
	cur := root
	res := make([]int, 0)
	for cur != nil || len(stk) != 0 {
		for cur != nil {
			stk = append(stk, cur)
			cur = cur.Left
		}
		cur = stk[len(stk)-1]
		res = append(res, cur.Val)
		stk = stk[:len(stk)-1]
		cur = cur.Right
	}
	return res
}

// @lc code=end

