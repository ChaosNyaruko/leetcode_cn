/*
 * @lc app=leetcode.cn id=2 lang=golang
 *
 * [2] 两数相加
 */

// @lc code=start
/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func addTwoNumbers(l1 *ListNode, l2 *ListNode) *ListNode {
	dummy := &ListNode{Val: 0, Next: nil}
	cur := dummy
	carry := 0
	for l1 != nil || l2 != nil {
		a := 0
		b := 0
		if l1 != nil {
			a = l1.Val
		}
		if l2 != nil {
			b = l2.Val
		}
		res := a + b + carry
		cur.Next = &ListNode{Val: res % 10}
		carry = res / 10
		cur = cur.Next
		if l1 != nil {
			l1 = l1.Next
		}
		if l2 != nil {
			l2 = l2.Next
		}
	}
	for carry != 0 {
		cur.Next = &ListNode{Val: carry % 10}
		carry = carry / 10
	}
	return dummy.Next
}

// @lc code=end

