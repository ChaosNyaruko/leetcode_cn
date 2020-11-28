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

func buildTree(preorder []int, inorder []int) *TreeNode {
	if len(preorder) == 0 {
		return nil
	}
	return helper(preorder, inorder, 0, len(preorder)-1, 0, len(inorder)-1)
}
