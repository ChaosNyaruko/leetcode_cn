/*
 * @lc app=leetcode.cn id=24 lang=golang
 *
 * [24] 两两交换链表中的节点
 */

// @lc code=start
/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func swapPairs(head *ListNode) *ListNode {
	dummy := &ListNode{0, head}
	pre, cur := dummy, head
	for cur != nil && cur.Next != nil {
		tmp := cur.Next.Next
		oriCurNext := cur.Next
		cur.Next.Next = cur
		cur.Next = tmp
		pre.Next = oriCurNext
		pre = cur
		cur = cur.Next
	}
	return dummy.Next
}

// @lc code=end

