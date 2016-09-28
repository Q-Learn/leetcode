# 107. Binary Tree Level Order Traversal II  QuestionEditorial Solution

# Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None: 
            return []
        result, level= [], [root]
        while level:
            result.append([node.val for node in level])
            level = [kid for node in level for kid in [node.left, node.right] if kid]
        result.reverse()
        return result    
