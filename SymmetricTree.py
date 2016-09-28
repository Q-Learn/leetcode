# 101. Symmetric Tree  QuestionEditorial Solution

# Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

# Bonus points if you could solve it both recursively and iteratively.



# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None: 
            return True
        return self.isMirror(root.left, root.right)
        
    def isMirror(self, left, right):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if left is None and right is None:
            return True
        if left is None or right is None:
            return False
        if left.val == right.val:
            return self.isMirror(left.left, right.right) and self.isMirror(left.right, right.left)
        else:
            return False 
        
