# -*- coding: utf-8 -*-

from collections import defaultdict

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    # Runtime 189 ms / Memory 21 MB
    def deepestLeavesSum_1(self, root):
        r = 0
        queue = [root]

        while (queue):
            temp = 0
            n = len(queue)
            for i in range(n):
                node = queue.pop(0)
                temp += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            r = temp
        
        return r

    # Runtime 195 ms / Memory 21 MB
    def deepestLeavesSum_2(self, root):
        levelDict = defaultdict(list)
        level = 0

        def dfs(node, depth):
            if not node:
                return
            
            levelDict[depth].append(node.val)
            dfs(node.left,depth+1)
            dfs(node.right,depth+1)
        
        dfs(root,level)
        level_max = max(levelDict.keys())

        return sum(levelDict[level_max])