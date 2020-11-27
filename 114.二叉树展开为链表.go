/*
 * @lc app=leetcode.cn id=114 lang=golang
 *
 * [114] 二叉树展开为链表
 */

// @lc code=start
/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNodej
 * }
 */

func flatten(root *TreeNode) {
	if root == nil {
		return
	}
	stk := []*TreeNode{root}
	var prev *TreeNode
	for len(stk) > 0 {
		cur := stk[len(stk)-1]
		stk = stk[:len(stk)-1]
		if prev != nil {
			prev.Left, prev.Right = nil, cur
		}
		if cur.Right != nil {
			stk = append(stk, cur.Right)
		}
		if cur.Left != nil {
			stk = append(stk, cur.Left)
		}
		prev = cur
	}
	return
}

// @lc code=end

