/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func mirrorTree(root *TreeNode) *TreeNode {
    if root == nil {
        return nil
    }
    left := mirrorTree(root.Left)
    right := mirrorTree(root.Right)
    root.Left, root.Right = right, left
    return root
}