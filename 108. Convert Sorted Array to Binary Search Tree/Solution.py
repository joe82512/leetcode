# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    # Runtime 129 ms / Memory 16.2 MB
    def sortedArrayToBST_1(self, nums):
        if not nums:
            return None
        else:
            p = len(nums)//2
            # n = TreeNode(nums[p])
            n = TreeNode()
            n.val = nums[p]            
            n.left = self.sortedArrayToBST_1(nums[:p])
            n.right = self.sortedArrayToBST_1(nums[p+1:])
            return n

    # Runtime 116 ms / Memory 16.2 MB
    def sortedArrayToBST_2(self, nums):
        return self.assingNode(nums,0,len(nums))
        
    def assingNode(self,nums,low,high):
        if low == high:
            return None
        else:
            mid = (low+high)//2
            node = TreeNode(nums[mid])
            node.left = self.assingNode(nums,low,mid)
            node.right = self.assingNode(nums,mid+1,high)
            return node



if __name__ == '__main__':
    print("=====================================")   