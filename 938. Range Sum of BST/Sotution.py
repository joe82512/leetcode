# -*- coding: utf-8 -*-

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    # Runtime 271 ms / Memory 29.6 MB
    def rangeSumBST_1(self, root, low, high):
        self.value = []
        def DFS(node):
            if not node:
                return
            DFS(node.left)
            self.value += [node.val]
            DFS(node.right)
            
        DFS(root)

        sum = 0
        for v in self.value:
            if high >= v >= low:
                sum = sum + v
        
        return sum
    
    
    # Runtime 183 ms / Memory 29.6 MB
    def rangeSumBST_2(self, root, low, high):
        self.res = 0
        def DFS(node):
            if not node:
                return
            
            if (node.val>low): #L
                DFS(node.left)

            if (high>=node.val>=low): #middle
                self.res += node.val
                print(node.val)

            if (high>node.val): #R
                DFS(node.right)
            
        DFS(root)

        return self.res