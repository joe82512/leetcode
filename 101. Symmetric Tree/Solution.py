# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    # Runtime 35 ms / Memory 13.5 MB
    def isSymmetric_1(self, root):
        # closure
        def isSym(L,R): 
            if L and R and L.val == R.val: 
                return isSym(L.left, R.right) and isSym(L.right, R.left)
            else:
                return L == R #both None or not equal
        # main
        if root:
            return isSym(root.left, root.right)
        else:
            return True

    # Runtime ms / Memory B
    def isSymmetric_2(self, head):
        pass



if __name__ == '__main__':
    print("=====================================")   