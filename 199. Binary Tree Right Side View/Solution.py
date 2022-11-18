# -*- coding: utf-8 -*-

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    # Runtime 33 ms / Memory 13.4 MB
    '''
    ref: https://leetcode.com/problems/binary-tree-right-side-view/solutions/2266055/c-python-explained/
    '''
    def rightSideView_1(self, root):
        def dfs(root,depth):
            if root:
                if len(res)==depth:
                    res.append(root.val)
                dfs(root.right, depth+1)
                dfs(root.left, depth+1)
            else:
                return 

        res = []
        dfs(root,0)
        return res

    # Runtime ms / Memory MB
    def rightSideView_2(self, root):
        pass