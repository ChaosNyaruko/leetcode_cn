/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func kthLargest(root *TreeNode, k int) int {
    res := 0
    var helper func(*TreeNode)
    helper = func(cur *TreeNode) {
        if cur == nil {
            return
        }
        helper(cur.Right)
        k -= 1
        if k == 0 {
            res = cur.Val
            return
        }
        helper(cur.Left)
    }
    helper(root)
    return res
}