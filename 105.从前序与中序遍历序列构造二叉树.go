/*
 * @lc app=leetcode.cn id=105 lang=golang
 *
 * [105] 从前序与中序遍历序列构造二叉树
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
func helper(preorder []int, inorder []int, preLeft, preRight, inLeft, inRight int) *TreeNode {
	if preLeft > preRight {
		return nil
	}
	if preLeft == preRight {
		return &TreeNode{Val: preorder[preLeft]}
	}
	root := &TreeNode{Val: preorder[preLeft]}
	// fmt.Println("-----root-----", root.Val)
	j := inLeft
	for ; j <= inRight; j++ {
		if inorder[j] == root.Val {
			break
		}
	}
	leftNum := j - inLeft
	root.Left = helper(preorder, inorder, preLeft+1, preLeft+leftNum, inLeft, j-1)
	root.Right = helper(preorder, inorder, preLeft+leftNum+1, preRight, j+1, inRight)
	return root
}

func buildTree_1(preorder []int, inorder []int) *TreeNode {
	if len(preorder) == 0 {
		return nil
	}
	return helper(preorder, inorder, 0, len(preorder)-1, 0, len(inorder)-1)
}

func buildTree(preorder []int, inorder []int) *TreeNode {
	if len(preorder) == 0 {
		return nil
	}
	root := &TreeNode{preorder[0], nil, nil}
	stack := []*TreeNode{}
	stack = append(stack, root)
	var inorderIndex int
	for i := 1; i < len(preorder); i++ {
		preorderVal := preorder[i]
		node := stack[len(stack)-1]
		if node.Val != inorder[inorderIndex] {
			node.Left = &TreeNode{preorderVal, nil, nil}
			stack = append(stack, node.Left)
		} else {
			for len(stack) != 0 && stack[len(stack)-1].Val == inorder[inorderIndex] {
				node = stack[len(stack)-1]
				stack = stack[:len(stack)-1]
				inorderIndex++
			}
			node.Right = &TreeNode{preorderVal, nil, nil}
			stack = append(stack, node.Right)
		}
	}
	return root
}

// @lc code=end

