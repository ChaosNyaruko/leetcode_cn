/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func deleteNode(head *ListNode, val int) *ListNode {
    dummy := &ListNode {
        Val: 0,
        Next: head,
    }
    prev := dummy
    cur := head
    for cur != nil {
        if cur.Val == val {
            prev.Next = cur.Next
            break
        }
        prev = cur
        cur = cur.Next
    }
    return dummy.Next
}