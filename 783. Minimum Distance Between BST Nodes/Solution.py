# -*- coding: utf-8 -*-

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    # Runtime 25 ms / Memory 13.8 MB
    def minDiffInBST_1(self, root):
        nodes = []
        def getNode(root):
            if root:
                getNode(root.left)
                nodes.append(root.val)
                getNode(root.right)
            else:
                return

        getNode(root)
        reduce_nodes = [nodes[i]-nodes[i-1] for i in range(1,len(nodes))]
        return min(reduce_nodes)

    # Runtime 9 ms / Memory 13.8 MB
    def minDiffInBST_2(self, root):
        self.prev = None
        self.r = int(1E5) #max
        def getNode(root):
            if root:
                getNode(root.left)
                if self.prev:
                    self.r = min(self.r, root.val-self.prev.val)
                self.prev = root
                getNode(root.right)
            else:
                return

        getNode(root)
        return self.r