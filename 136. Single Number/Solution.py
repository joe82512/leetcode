# -*- coding: utf-8 -*-
class Solution:
    # Runtime 109 ms / Memory 15.7 MB
    def singleNumber_1(self, nums):
        nums = sorted(nums)
        for i in range(1,len(nums),2):
            if nums[i] != nums[i-1]: #odd != even
                return nums[i-1] #odd
        return nums[-1] # last

    # Runtime 102 ms / Memory 15.6 MB
    def singleNumber_2(self, nums):
        result = nums[0]
        for i in range(1, len(nums)):
            result ^= nums[i] #XOR
        return result



if __name__ == '__main__':
    print(Solution().singleNumber_1([2,2,1]))
    print(Solution().singleNumber_1([4,1,2,1,2]))
    print(Solution().singleNumber_1([1]))
    print("=====================================")
    print(Solution().singleNumber_2([2,2,1]))
    print(Solution().singleNumber_2([4,1,2,1,2]))
    print(Solution().singleNumber_2([1]))