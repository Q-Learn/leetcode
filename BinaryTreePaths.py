# 257. Binary Tree Paths  QuestionEditorial Solution

# Given a binary tree, return all root-to-leaf paths.





# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {string[]}
    def binaryTreePaths(self, root):
        if not root:
            return []
        if not root.left and not root.right: 
            return [str(root.val)]
        return [str(root.val) + '->' + path
                for kid in (root.left, root.right) if kid
                for path in self.binaryTreePaths(kid)]
