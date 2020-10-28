import "fmt"

/*
 * @lc app=leetcode.cn id=25 lang=golang
 *
 * [25] K 个一组翻转链表
 */

// @lc code=start
/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func reverseKGroup(head *ListNode, k int) *ListNode {
	dummy := &ListNode{0, head}
	cur := dummy
	len := 0
	for cur.Next != nil {
		cur = cur.Next
		len++
	}
	// fmt.Println(len)
	cur = dummy
	for i := 0; i < len/k; i++ {
		lastStart, lastEnd := reverseK(cur.Next, k)
		// fmt.Println(lastStart.Val, lastEnd.Val)
		cur.Next = lastStart
		cur = lastEnd
	}
	return dummy.Next
}

// reverseK 输出翻转后的起始和终点
func reverseK(head *ListNode, k int) (*ListNode, *ListNode) {
	dummy := &ListNode{0, head}
	cur := dummy.Next
	cnt := 0
	for cnt < k-1 {
		then := cur.Next
		cur.Next = then.Next
		then.Next = dummy.Next
		dummy.Next = then
		cnt++
	}
	return dummy.Next, cur
}

// @lc code=end

