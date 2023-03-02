# -*- coding: utf-8 -*-
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    # Runtime 23 ms / Memory 13.4 MB
    def invertTree_1(self, root):
        if root:
            self.invertTree(root.left)
            self.invertTree(root.right)
            root.left, root.right = root.right, root.left
            return root
        else:
            return

    # Runtime ms / Memory MB
    def invertTree_2(self, root):
        pass