class Solution(object):
    # Runtime 196 ms / Memory 21.7 MB
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        if (max(nums)>=target):
            return 1
        #else:
        res = len(nums)+1 #more than impossible
        temp_sum = 0
        L, R = 0, 0
        for R in range(len(nums)):
            temp_sum += nums[R] #slide window
            while (temp_sum>=target): #early break
                res = min(res, (R-L+1))
                temp_sum -= nums[L]
                L = L+1
        
        if res > len(nums):
            return 0
        else:
            return res
    """
    暴力法超時
        if (max(nums)>=target):
            return 1
        #else:
        res = len(nums)+1 #more than impossible
        temp_sum = 0
        for i in range(len(nums)):
            temp_sum = nums[i] #worst
            for j in range(i+1,len(nums)):
                temp_sum += nums[j]
                if (temp_sum>=target):
                    res = min(res,j-i+1)
                    break
        if res > len(nums):
            return 0
        else:
            return res
    """