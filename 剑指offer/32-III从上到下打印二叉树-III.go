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
    stk := [2][]*TreeNode{}
    stk[0] = []*TreeNode{root}
    stk[1] = make([]*TreeNode, 0)
    res := make([][]int, 0)

    current := 0
    next := 1 - current
    level := make([]int, 0)
    for len(stk[0]) != 0 || len(stk[1]) != 0 {
        cur := stk[current][len(stk[current]) - 1]
        stk[current] = stk[current][:len(stk[current]) - 1]
        if current == 0 {
            if cur.Left != nil {
                stk[next] = append(stk[next], cur.Left)
            }
            if cur.Right != nil {
                stk[next] = append(stk[next], cur.Right)
            }
        } else {
            if cur.Right != nil {
                stk[next] = append(stk[next], cur.Right)
            }
            if cur.Left != nil {
                stk[next] = append(stk[next], cur.Left)
            }
        }
        level = append(level, cur.Val)
        if len(stk[current]) == 0 {
            current = 1 - current
            next = 1 - current
            tmp := make([]int, len(level))
            copy(tmp, level)
            level = level[:0]
            res = append(res, tmp)
        }
    }
    return res
}