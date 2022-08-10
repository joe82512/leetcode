# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    # Runtime 50 ms / Memory 16.1 MB
    def maxDepth_1(self, root):
        return max(self.maxDepth_1(root.left), self.maxDepth_1(root.right)) + 1 if root else 0

    # Runtime 52 ms / Memory 16.3 MB
    def maxDepth_2(self, root):
        if root == None:
            return 0
        depth = 0
        r_list = [root]
        while len(r_list)>0:
            temp_list = []
            depth += 1
            for node in r_list:
                if node.left:
                    temp_list.append(node.left)
                if node.right:
                    temp_list.append(node.right)
            
            r_list = temp_list
        return depth



if __name__ == '__main__':
    print("=====================================")   