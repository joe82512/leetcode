# -*- coding: utf-8 -*-
class Solution:
    # Runtime 944 ms / Memory 25.5 MB
    def maxSubArray_1(self, nums):
        max_sum = nums[0]
        temp_sum = nums[0]
        for i in range(1, len(nums)):
            temp_sum = max(nums[i]+temp_sum, nums[i]) #update or reset
            max_sum = max(temp_sum, max_sum)
        return max_sum

    # Runtime 592 ms / Memory 25.6 MB    
    def maxSubArray_2(self, nums):
        for i in range(1, len(nums)):
            nums[i] = max(nums[i]+nums[i-1], nums[i])
        return max(nums) # same as max_sum = max(temp_sum, max_sum)



if __name__ == '__main__':
    print(Solution().maxSubArray_1([-2,1,-3,4,-1,2,1,-5,4]))
    print(Solution().maxSubArray_1([1]))
    print(Solution().maxSubArray_1([5,4,-1,7,8]))
    print("=====================================")
    print(Solution().maxSubArray_2([-2,1,-3,4,-1,2,1,-5,4]))
    print(Solution().maxSubArray_2([1]))
    print(Solution().maxSubArray_2([5,4,-1,7,8]))