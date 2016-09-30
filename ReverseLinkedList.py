# 206. Reverse Linked List  QuestionEditorial Solution

# Reverse a singly linked list.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return head
            
        pointer = head.next
        head.next = None

        while pointer:
            tmp = head
            head = pointer
            pointer = pointer.next
            head.next = tmp
        return head
