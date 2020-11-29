/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func levelOrder(root *TreeNode) []int {
    if root == nil {
        return nil
    }
    q := []*TreeNode{root}
    res := make([]int, 0)
    for len(q) != 0 {
        front := q[0]
        if front.Left != nil {
            q = append(q, front.Left)
        }
        if front.Right != nil {
            q = append(q, front.Right)
        }
        q = q[1:]
        res = append(res, front.Val)
    }
    return res
}