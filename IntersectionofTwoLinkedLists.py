# 160. Intersection of Two Linked Lists  QuestionEditorial Solution

# Write a program to find the node at which the intersection of two singly linked lists begins.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        lenA, nodeA = 0, headA
        while nodeA:
            lenA += 1
            nodeA = nodeA.next
            
        lenB, nodeB = 0, headB
        while nodeB:
            lenB += 1
            nodeB = nodeB.next
            
        nodeA, nodeB = headA, headB
        if lenA <= lenB:
            short, long = headA, headB
        else:
            short, long = headB, headA
        for _ in range(abs(lenB-lenA)):
            long = long.next
        while short:
            if short == long:
                return short
            short = short.next
            long = long.next
        return None
