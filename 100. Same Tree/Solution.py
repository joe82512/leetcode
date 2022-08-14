# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    # Runtime 24 ms / Memory 13.5 MB
    def isSameTree_1(self, p, q):
        if p and q:            
            if p.val != q.val:
                return False                
            else:
                return self.isSameTree_1(p.left,q.left) & self.isSameTree_1(p.right,q.right)
        
        else:
            return (p==q) # both none or not equal

    # Runtime ms / Memory B
    def isSameTree_2(self, head):
        pass



if __name__ == '__main__':
    print("=====================================")   