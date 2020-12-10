#
# @lc app=leetcode.cn id=148 lang=python3
#
# [148] 排序链表
#
# https://leetcode-cn.com/problems/sort-list/description/
#
# algorithms
# Medium (67.87%)
# Likes:    921
# Dislikes: 0
# Total Accepted:    126.8K
# Total Submissions: 186.9K
# Testcase Example:  '[4,2,1,3]'
#
# 给你链表的头结点 head ，请将其按 升序 排列并返回 排序后的链表 。
# 
# 进阶：
# 
# 
# 你可以在 O(n log n) 时间复杂度和常数级空间复杂度下，对链表进行排序吗？
# 
# 
# 
# 
# 示例 1：
# 
# 
# 输入：head = [4,2,1,3]
# 输出：[1,2,3,4]
# 
# 
# 示例 2：
# 
# 
# 输入：head = [-1,5,3,4,0]
# 输出：[-1,0,3,4,5]
# 
# 
# 示例 3：
# 
# 
# 输入：head = []
# 输出：[]
# 
# 
# 
# 
# 提示：
# 
# 
# 链表中节点的数目在范围 [0, 5 * 10^4] 内
# -10^5 
# 
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        def helper(head, tail):
            if not head:
                return head
            if head.next == tail:
                head.next = None
                return head
            slow = fast = head
            while fast != tail:
                slow = slow.next
                fast = fast.next
                if fast != tail:
                    fast = fast.next
            mid = slow
            return merge(helper(head, mid), helper(mid, tail))

        def merge(h1, h2):
            dummy = ListNode(0)
            cur, p1, p2 = dummy, h1, h2
            while p1 and p2:
                if p1.val < p2.val:
                    cur.next = p1
                    p1 = p1.next
                else:
                    cur.next = p2
                    p2 = p2.next
                cur = cur.next
            if p1:
                cur.next = p1
            if p2:
                cur.next = p2
            return dummy.next
        return helper(head, None)


# @lc code=end

