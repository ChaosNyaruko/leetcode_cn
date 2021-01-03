#
# @lc app=leetcode.cn id=86 lang=python3
#
# [86] 分隔链表
#
# https://leetcode-cn.com/problems/partition-list/description/
#
# algorithms
# Medium (60.87%)
# Likes:    309
# Dislikes: 0
# Total Accepted:    65.2K
# Total Submissions: 107.4K
# Testcase Example:  '[1,4,3,2,5,2]\n3'
#
# 给你一个链表和一个特定值 x ，请你对链表进行分隔，使得所有小于 x 的节点都出现在大于或等于 x 的节点之前。
# 
# 你应当保留两个分区中每个节点的初始相对位置。
# 
# 
# 
# 示例：
# 
# 
# 输入：head = 1->4->3->2->5->2, x = 3
# 输出：1->2->2->4->3->5
# 
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        if not head:
            return None
        cur = head
        smallCur = smallerHead = ListNode(0)
        bigCur = bigHead = ListNode(0)
        while cur:
            if cur.val < x:
                smallCur.next = cur
                smallCur = smallCur.next
            else:
                bigCur.next = cur
                bigCur = bigCur.next
            cur = cur.next
        smallCur.next = bigHead.next
        bigCur.next = None
        return smallerHead.next


# @lc code=end

