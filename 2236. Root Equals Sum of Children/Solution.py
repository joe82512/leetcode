# -*- coding: utf-8 -*-
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    # Runtime 41 ms / Memory 13.3 MB
    def checkTree_1(self, root):
        return root.val == (root.left.val + root.right.val)

    # Runtime ms / Memory MB
    def checkTree_2(self, root):
        pass



if __name__ == '__main__':
    print("=====================================")