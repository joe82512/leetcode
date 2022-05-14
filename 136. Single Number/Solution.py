# -*- coding: utf-8 -*-
class Solution:
    # Runtime 109 ms / Memory 15.7 MB
    def singleNumber_1(self, nums):
        nums = sorted(nums)
        for i in range(1,len(nums),2):
            if nums[i] != nums[i-1]:
                return nums[i-1]
        return nums[-1] # last

    # Runtime  / Memory 
    def maxSubArray_2(self, nums):
        pass



if __name__ == '__main__':
    print(Solution().singleNumber_1([2,2,1]))
    print(Solution().singleNumber_1([4,1,2,1,2]))
    print(Solution().singleNumber_1([1]))
    print("=====================================")
    print(Solution().singleNumber_2([2,2,1]))
    print(Solution().singleNumber_2([4,1,2,1,2]))
    print(Solution().singleNumber_2([1]))