/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

// helper: 以A为根节点的子树是否包含B
// A必须是根节点
func helper(A *TreeNode, B *TreeNode) bool {
    if B == nil {
        return true
    }
    if A == nil {
        return false
    }
    if A.Val != B.Val {
        return false
    }
    return helper(A.Left, B.Left) && helper(A.Right, B.Right)
}
func isSubStructure(A *TreeNode, B *TreeNode) bool {
    if B == nil {
        return false
    }

    if A == nil {
        return false
    }

    if helper(A, B) {
        return true
    }

    if isSubStructure(A.Left, B) || isSubStructure(A.Right, B) {
        return true
    }

    return false
}