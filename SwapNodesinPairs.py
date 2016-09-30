# 24. Swap Nodes in Pairs  QuestionEditorial Solution

# Given a linked list, swap every two adjacent nodes and return its head.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        tail = dummy = ListNode(0)
        dummy.next = head
        while tail.next and tail.next.next:
            tmp1 = tail.next.next
            tmp2 = tmp1.next
            tmp1.next = tail.next
            tail.next.next = tmp2
            tail.next = tmp1
            tail = tail.next.next
        return dummy.next
