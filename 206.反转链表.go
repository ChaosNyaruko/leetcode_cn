/*
 * @lc app=leetcode.cn id=206 lang=golang
 *
 * [206] 反转链表
 *
 * https://leetcode-cn.com/problems/reverse-linked-list/description/
 *
 * algorithms
 * Easy (71.01%)
 * Likes:    1368
 * Dislikes: 0
 * Total Accepted:    379.8K
 * Total Submissions: 534.8K
 * Testcase Example:  '[1,2,3,4,5]'
 *
 * 反转一个单链表。
 * 
 * 示例:
 * 
 * 输入: 1->2->3->4->5->NULL
 * 输出: 5->4->3->2->1->NULL
 * 
 * 进阶:
 * 你可以迭代或递归地反转链表。你能否用两种方法解决这道题？
 * 
 */

// @lc code=start
/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func reverseList_1(head *ListNode) *ListNode {
    if head == nil {
        return nil
    }
    dummy := &ListNode{0, head}
    prev := dummy
    cur := head
    for cur != nil {
        next := cur.Next
        cur.Next = prev
        prev = cur
        cur = next
    }
    head.Next = nil
    return prev
}

// 递归解法
func reverseList(head *ListNode) *ListNode {
	if head == nil  || head.Next == nil{
		return head
	}
	ret := reverseList(head.Next)
	head.Next.Next = head
	head.Next = nil
	return ret
}
// @lc code=end

