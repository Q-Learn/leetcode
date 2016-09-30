# 234. Palindrome Linked List  QuestionEditorial Solution

# Given a singly linked list, determine if it is a palindrome.

# Could you do it in O(n) time and O(1) space?



# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # Method 2:
        # Time~O(n) Memory~O(1)
        
        # find mid point
        if head==None:
            return True
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        # reverse second half
        pointer = slow.next
        slow.next = None
        while pointer:
            tmp = slow
            slow = pointer
            pointer = pointer.next
            slow.next = tmp
            
        # compare
        while slow:
            if slow.val != head.val:
                return False
            slow = slow.next
            head = head.next
        return True
            
        
        """
        # Method 1: 
        # Time~O(n) Memory~O(n)
        arr = []
        while head:
            arr.append(head.val)
            head = head.next
        return arr == arr[::-1]
        """
        
        
