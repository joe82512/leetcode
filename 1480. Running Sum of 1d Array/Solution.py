# -*- coding: utf-8 -*-
class Solution:
    # Runtime 28 ms / Memory 13.5 MB
    def runningSum_1(self, nums):
        n0 = 0
        new_nums = []
        for n in nums:
            n0 += n
            new_nums.append(n0)
        return new_nums

    # Runtime 54 ms / Memory 13.5 MB
    def runningSum_2(self, nums):
        for idx in range(1,len(nums)):
            nums[idx] += nums[idx-1]
        return nums



if __name__ == '__main__':
    print(Solution().runningSum_1([1,2,3,4]))
    print(Solution().runningSum_1([1,1,1,1,1]))
    print(Solution().runningSum_1([3,1,2,10,1]))
    print("=====================================")
    print(Solution().runningSum_2([1,2,3,4]))
    print(Solution().runningSum_2([1,1,1,1,1]))
    print(Solution().runningSum_2([3,1,2,10,1]))