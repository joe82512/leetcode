class Solution(object):
    # Runtime 181 ms / Memory 21.4 MB
    def productExceptSelf_1(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        #[a,b,c,d]
        left = [1]*len(nums)
        for i in range(1,len(nums)):
            left[i] = left[i-1]*nums[i-1] #[1,a,ab,abc]
        

        right = [1]*len(nums)
        for j in range(len(nums)-2,-1,-1):
            right[j] = right[j+1]*nums[j+1] #[bcd,cd,d,1]

        res = [ left[k]*right[k] for k in range(len(nums))]
        return res
    
    # Runtime 163 ms / Memory 18.7 MB
    def productExceptSelf_2(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = [1]*len(nums)
        prod = 1
        for i in range(1,len(nums)):
            res[i] = res[i-1]*nums[i-1]
        
        for j in range(len(nums)-1,-1,-1):
            res[j] = res[j]*prod
            prod = prod*nums[j]
        return res