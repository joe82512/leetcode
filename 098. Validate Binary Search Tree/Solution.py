# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    # Runtime 47 ms / Memory 18 MB
    def isValidBST_1(self, root):
        def traverse(root, low, high):
            if not root: #None, mean step to bottom
                return True
            elif not low < root.val < high: #Compare Condition
                # ref: https://ithelp.ithome.com.tw/articles/10213279
                return False
            else:
                # keep root as low and high, update root
                return traverse(root.left, low, root.val) and traverse(root.right, root.val, high)
        return traverse(root,low=float('-inf'),high=float('inf'))

    # Runtime ms / Memory B
    def isValidBST_2(self, head):
        pass



if __name__ == '__main__':
    print("=====================================")   