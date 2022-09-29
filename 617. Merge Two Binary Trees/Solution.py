# -*- coding: utf-8 -*-
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    # Runtime 211 ms / Memory 14.5 MB
    def mergeTrees_1(self, root1, root2):
        result = TreeNode()
        # if (root1 == None) and (root2 == None):
        #     result = None
        if root1 == None:
            result = root2 #not result.val = root2.val
            # root2 maybe None
        elif root2 == None:
            result = root1
        else:
            result.val = root1.val + root2.val                
            result.left = self.mergeTrees_1(root1.left,root2.left)
            result.right = self.mergeTrees_1(root1.right,root2.right)
        
        return result

    # Runtime 209 ms / Memory 14.8 MB
    def mergeTrees_2(self, root1, root2):
        if (root1 == None) and (root2 == None):
            return None
        else:
            result = TreeNode((root1.val if root1 else 0) + (root2.val if root2 else 0))         
            result.left = self.mergeTrees_2(root1 and root1.left, root2 and root2.left)
            result.right = self.mergeTrees_2(root1 and root1.right, root2 and root2.right)
            return result



if __name__ == '__main__':
    print("=====================================")