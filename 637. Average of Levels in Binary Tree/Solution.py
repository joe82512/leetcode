# -*- coding: utf-8 -*-

from collections import defaultdict

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    # Runtime 36 ms / Memory 18 MB
    def averageOfLevels_1(self, root):
        r = []
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
            
            r.append(float(temp)/n)
        
        return r

    # Runtime 39 ms / Memory 18.7 MB
    def averageOfLevels_2(self, root):
        levelDict = defaultdict(list)
        level = 0

        def dfs(node, depth):
            if not node:
                return
            
            levelDict[depth].append(node.val)
            dfs(node.left,depth+1)
            dfs(node.right,depth+1)
        
        dfs(root,level)
        level_avg = [float(sum(v))/len(v) for v in levelDict.values()]

        return level_avg