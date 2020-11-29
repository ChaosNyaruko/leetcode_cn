/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func pathSum(root *TreeNode, sum int) [][]int {
    if root == nil {
        return nil
    }
    path := make([]int, 0)
    res := make([][]int, 0)
    var helper func(*TreeNode, []int, int)
    helper = func(cur *TreeNode, path []int, curSum int) {
        if cur == nil {
            return
        }
        curSum += cur.Val
        path = append(path, cur.Val)

        if cur.Left == nil && cur.Right == nil {
            if curSum == sum {
                tmp := make([]int, len(path))
                copy(tmp, path)
                res = append(res, tmp)
            }
            path = path[:len(path) - 1]
            // curSum -= cur.Val
            return
        }
        helper(cur.Left, path, curSum)
        helper(cur.Right, path, curSum) 
        path = path[:len(path) - 1]
        // curSum -= cur.Val
    }
    helper(root, path, 0)
    return res
}