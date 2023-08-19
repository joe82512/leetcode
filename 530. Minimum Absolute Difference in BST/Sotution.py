# -*- coding: utf-8 -*-

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    # Runtime 45 ms / Memory 17.6 MB
    def getMinimumDifference_1(self, root):
        self.value = []
 
        def DFS(node):
            if not node:
                return
            DFS(node.left)
            self.value += [node.val]
            DFS(node.right)

        DFS(root)
        
        delta_min = float("inf")
        c0 = self.value.pop(0)
        for c in self.value:
            delta_min = min(delta_min,(c-c0))
            c0 = c
        
        return delta_min
    

    # Runtime 30 ms / Memory 17.2 MB
    res = float("inf")
    temp = float("-inf")
    def getMinimumDifference_2(self, root):
        if not root:
            return 0
        
        self.getMinimumDifference_2(root.left)
        self.res = min(self.res, root.val-self.temp)
        self.temp = root.val
        self.getMinimumDifference_2(root.right)

        return self.res