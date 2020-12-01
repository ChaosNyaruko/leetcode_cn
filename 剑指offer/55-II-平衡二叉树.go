/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func max(a, b int) int {
    if a > b {
        return a
    }
    return b
}
// 后序遍历，自底向上同时返回子树是否是平衡的以及子树深度
func helper(root *TreeNode) (bool, int) {
    if root == nil {
        return true, 0
    }
    leftBalanced, leftDepth := helper(root.Left)
    if leftBalanced == false {
        return false, -1
    }
    rightBalanced, rightDepth := helper(root.Right)
    if rightBalanced == false {
        return false, -1
    }
    diff := leftDepth - rightDepth
    if diff >= -1 && diff <=1 {
        return true, max(leftDepth, rightDepth) + 1
    }
    return false, -1
}
func isBalanced(root *TreeNode) bool {
    res, _ := helper(root)
    return res
}