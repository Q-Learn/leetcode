# 102. Binary Tree Level Order Traversal  QuestionEditorial Solution

# Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).




# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
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
        return result
                

