# -*- coding: utf-8 -*-

# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution(object):
    # Runtime 39 ms / Memory 16.5 MB
    def maxDepth_1(self, root):
        level = 0
        queue = [root]
        if not root:
            return 0
        while queue:
            level += 1
            n = len(queue)
            for i in range(n): #calculate depth
                node = queue.pop(0)
                for child in node.children:
                    queue.append(child)
        
        return level

    # Runtime 47 ms / Memory 16.2 MB
    def maxDepth_2(self, root):
        if not root:
            return 0
        max_depth = 0
        for child in root.children:
            max_depth = max(max_depth, self.maxDepth_2(child))
        return max_depth + 1
