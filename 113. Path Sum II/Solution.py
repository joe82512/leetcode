# -*- coding: utf-8 -*-
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    # Runtime 74 ms / Memory 20.4 MB
    def pathSum_1(self, root, targetSum):
        def DFS(node,target,path,res):
            if not node:
                return
            path.append(node.val)
            if not node.left and not node.right and target==node.val:
                res.append(path)
                return
            DFS(node.left,target-node.val,path[:],res) #must path[:],deepcopy
            DFS(node.right,target-node.val,path[:],res)
            path.pop()
        
        res = []
        path = []
        DFS(root,targetSum,path,res)
        return res

    # Runtime ms / Memory MB
    def pathSum_2(self, root, targetSum):
        pass