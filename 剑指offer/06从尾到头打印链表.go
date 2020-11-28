/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func reversePrint_1(head *ListNode) []int {
	stk := make([]*ListNode, 0)
	for head != nil {
		stk = append(stk, head)
		head = head.Next
	}
	res := make([]int, 0, len(stk))
	for len(stk) != 0 {
		res = append(res, stk[len(stk) - 1].Val)
		stk = stk[:len(stk) - 1]
	}
	return res
}

func reversePrint(head *ListNode) []int {
	if head == nil {
		return []int{}
	}
	res := append(reversePrint(head.Next), head.Val)
	return res
}