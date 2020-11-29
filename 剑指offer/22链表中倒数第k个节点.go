/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func getKthFromEnd(head *ListNode, k int) *ListNode {
    dummy := &ListNode{Val:0, Next: head}
    fast := dummy
    for i := 0; i < k && fast != nil; i++ {
        fast = fast.Next
    }

    slow := dummy
    for fast != nil {
        slow = slow.Next
        fast = fast.Next
    }
    return slow
}