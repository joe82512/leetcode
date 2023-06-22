# -*- coding: utf-8 -*-

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    # Runtime 12 ms / Memory 13.3 MB
    def binaryTreePaths_1(self, root):
        result = []
        stack = [(root,"")]
        
        while (stack):
            (node,s) = stack.pop()
            if s!="":
                s = s + "->"
            if (node.left):
                stack.append( [node.left, s+str(node.val)] )
            if (node.right):
                stack.append( [node.right, s+str(node.val)] )
            if not (node.left) and not (node.right):
                result.append(s+str(node.val))

        return result

    # Runtime 7 ms / Memory 13.4 MB
    def binaryTreePaths_2(self, root):
        res = []
        
        def dfs(node, s):
            s += str(node.val)
            if node.left:
                dfs(node.left, s + "->")
            if node.right:
                dfs(node.right, s + "->")
            if not node.left and not node.right:
                res.append(s)
        
        dfs(root, "") 

        return res