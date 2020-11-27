/*
 * @lc app=leetcode.cn id=114 lang=golang
 *
 * [114] 二叉树展开为链表
 */

// @lc code=start
/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNodej
 * }
 */

func flatten_1(root *TreeNode) {
	if root == nil {
		return
	}
	stk := []*TreeNode{root}
	var prev *TreeNode
	for len(stk) > 0 {
		cur := stk[len(stk)-1]
		stk = stk[:len(stk)-1]
		if prev != nil {
			prev.Left, prev.Right = nil, cur
		}
		if cur.Right != nil {
			stk = append(stk, cur.Right)
		}
		if cur.Left != nil {
			stk = append(stk, cur.Left)
		}
		prev = cur
	}
	return
}

/*
前两种方法都借助前序遍历，前序遍历过程中需要使用栈存储节点。有没有空间复杂度是
O(1) 的做法呢？

注意到前序遍历访问各节点的顺序是根节点、左子树、右子树。如果一个节点的左子节点为空，则该节点不需要进行展开操作。如果一个节点的左子节点不为空，则该节点的左子树中的最后一个节点被访问之后，该节点的右子节点被访问。该节点的左子树中最后一个被访问的节点是左子树中的最右边的节点，也是该节点的前驱节点。因此，问题转化成寻找当前节点的前驱节点。

具体做法是，对于当前节点，如果其左子节点不为空，则在其左子树中找到最右边的节点，作为前驱节点，将当前节点的右子节点赋给前驱节点的右子节点，然后将当前节点的左子节点赋给当前节点的右子节点，并将当前节点的左子节点设为空。对当前节点处理结束后，继续处理链表中的下一个节点，直到所有节点都处理结束。

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/flatten-binary-tree-to-linked-list/solution/er-cha-shu-zhan-kai-wei-lian-biao-by-leetcode-solu/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
*/

func flatten(root *TreeNode) {
	cur := root
	for cur != nil {
		if cur.Left != nil {
			subCur := cur.Left
			for subCur != nil && subCur.Right != nil {
				subCur = subCur.Right
			}
			subCur.Right = cur.Right
			cur.Right = cur.Left
			cur.Left = nil
		}
		cur = cur.Right
	}
}

// @lc code=end

