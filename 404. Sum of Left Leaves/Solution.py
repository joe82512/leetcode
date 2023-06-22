# -*- coding: utf-8 -*-

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    # Runtime 15 ms / Memory 14.1 MB
    def sumOfLeftLeaves_1(self, root):     
        self.r = 0 
        def dfs(root, isLeft):
            if not root:
                return
            elif isLeft and not root.left and not root.right: 
                self.r += root.val
            dfs(root.left,  1)
            dfs(root.right, 0)
        
        dfs(root, 0)
        return self.r

    # Runtime 23 ms / Memory 14.1 MB
    def sumOfLeftLeaves_2(self, root):
        def dfs(root, isLeft):
            if not root:
                return 0
            elif not root.left and not root.right:
                if isLeft:
                    return root.val
                else:
                    return 0 
                self.r += root.val
            return dfs(root.left, 1) + dfs(root.right, 0)
        
        return dfs(root, 0)