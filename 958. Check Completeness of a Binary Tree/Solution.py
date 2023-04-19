# -*- coding: utf-8 -*-
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    # Runtime 19 ms / Memory 13.5 MB
    def isCompleteTree_1(self, root):
        queue = []
        null_flag = 0
        queue.append(root)
        while queue:
            node = queue.pop(0)
            if not node:
                null_flag = 1
            elif node and null_flag==1:
                return False
            else:
                queue.append(node.left)
                queue.append(node.right)
        return True

    # Runtime 28 ms / Memory 13.6 MB
    def isCompleteTree_2(self, root):
        if not root:
            return
        cnt = 1
        loc = [1] #location
        self.DFS(root,cnt,loc)
        loc.sort()
        for i,p in enumerate(loc):
            if i+1!=p:
                return False
        return True

    def DFS(self,root,cnt,loc):
        if root.left:
            loc.append(cnt*2)
            self.DFS(root.left,cnt*2,loc)
        if root.right:
            loc.append(cnt*2+1)
            self.DFS(root.right,cnt*2+1,loc)