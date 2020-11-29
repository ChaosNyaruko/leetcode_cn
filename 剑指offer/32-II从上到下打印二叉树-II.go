/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func levelOrder(root *TreeNode) [][]int {
    if root == nil {
        return nil
    }
    q := []*TreeNode{root}
    res := make([][]int, 0)
    level := make([]int, 0)
    curLevelToBeAdd := 1
    nextLevelToBeAdd := 0
    for len(q) != 0 {
        front := q[0]
        if front.Left != nil {
            q = append(q, front.Left)
            nextLevelToBeAdd++
        }
        if front.Right != nil {
            q = append(q, front.Right)
            nextLevelToBeAdd++
        }
        q = q[1:]
        curLevelToBeAdd--
        level = append(level, front.Val)
        if curLevelToBeAdd == 0 {
            tmp := make([]int, len(level))
            copy(tmp, level)
            res = append(res, tmp)
            level = level[:0]
            curLevelToBeAdd = nextLevelToBeAdd
            nextLevelToBeAdd = 0
        }
    }
    return res
}