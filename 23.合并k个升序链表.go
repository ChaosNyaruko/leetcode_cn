/*
 * @lc app=leetcode.cn id=23 lang=golang
 *
 * [23] 合并K个升序链表
 */

// @lc code=start
/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func merge2List(l1, l2 *ListNode) *ListNode {
	if l1 == nil {
		return l2
	} else if l2 == nil {
		return l1
	} else {
		if l1.Val < l2.Val {
			l1.Next = merge2List(l1.Next, l2)
			return l1
		} else {
			l2.Next = merge2List(l1, l2.Next)
			return l2
		}
	}
}

func mergeKLists(lists []*ListNode) *ListNode {
	r := len(lists) - 1
	if r < 0 {
		return nil
	}
	for r > 0 {
		l := 0
		for l < r {
			lists[l] = merge2List(lists[l], lists[r])
			l++
			r--
		}
	}
	return lists[0]
}

// @lc code=end

