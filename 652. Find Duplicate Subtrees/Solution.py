# -*- coding: utf-8 -*-
from collections import defaultdict
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    # Runtime 43 ms / Memory 26.8 MB
    def findDuplicateSubtrees_1(self, root):
        def DFS(node):
            if (node):
                key = str(node.val)+","+DFS(node.left)+","+DFS(node.right)
                cnt[key] += 1
                if cnt[key] == 2:
                    r.append(node)
                return key
                '''
                if key in cnt:
                    cnt[key] = cnt[key] + 1
                    if cnt[key] == 2:
                        r.append(node)
                else:
                    cnt[key] = 1
                return key
                '''
            else:
                return "None"

        cnt = defaultdict(int)
        r = []
        DFS(root)
        return r

    # Runtime 110 ms / Memory 16.2 MB
    def findDuplicateSubtrees_2(self, root):
        def DFS(node):
            if (node):
                key = ((node.val),DFS(node.left),DFS(node.right))
                cnt[key] += 1
                if cnt[key] == 2:
                    r.append(node)
                return key
            else:
                return None

        cnt = defaultdict(int)
        r = []
        DFS(root)
        return r