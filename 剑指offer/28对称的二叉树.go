/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func helper(p1, p2 *TreeNode) bool {
    if p1 == nil {
        return p2 == nil
    }
    if p2 == nil {
        return p1 == nil
    }
    if p1.Val != p2.Val {
        return false
    }
    return helper(p1.Left, p2.Right) && helper(p1.Right, p2.Left)
}

func isSymmetric(root *TreeNode) bool {
    if root == nil {
        return true
    }
    return helper(root.Left, root.Right)
}