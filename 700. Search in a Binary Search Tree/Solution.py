# -*- coding: utf-8 -*-

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    # Runtime 70 ms / Memory 17.2 MB
    def searchBST_1(self, root, val):
        queue = [root]
        while queue:
            node = queue.pop(0)
            if node.val==val:
                return node
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    # Runtime 60 ms / Memory 17.3 MB
    def searchBST_2(self, root, val):
        node = root
        while node:
            if node.val==val:
                return node
            elif node.val < val: #BST
                node = node.right
            else:
                node = node.left