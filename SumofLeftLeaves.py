# 404. Sum of Left Leaves  QuestionEditorial Solution

# Find the sum of all left leaves in a given binary tree.




# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None: 
            return 0
            
        if root.left and root.left.left is None and root.left.right is None:
            return root.left.val + self.sumOfLeftLeaves(root.right)
        else: 
            return self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right)
