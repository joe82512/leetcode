# -*- coding: utf-8 -*-
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    # Runtime 90 ms / Memory 21.2 MB
    def kthSmallest_1(self, root, k):
        count = []
        self.DFS(root, count)
        return count[k-1]

    def DFS(self, node, count):
        if not node:
            return
        self.DFS(node.left, count)
        count.append(node.val)
        self.DFS(node.right, count)

    # Runtime 36 ms / Memory 21.2 MB
    def kthSmallest_2(self, root, k):
        self.result = 0
        self.k = k
        self.DFS2(root)
        return self.result

    def DFS2(self, node):
        if node:
            self.DFS2(node.left)
            self.k -= 1
            if self.k == 0:
                self.result = node.val
                return
            self.DFS2(node.right)