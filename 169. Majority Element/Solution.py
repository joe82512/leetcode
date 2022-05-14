# -*- coding: utf-8 -*-
class Solution:
    # Runtime 176 ms / Memory 14.7 MB
    def majorityElement_1(self, nums):
        nums = sorted(nums)
        return nums[int(len(nums)/2)]

    # Runtime  / Memory 
    def majorityElement_2(self, nums):
        pass



if __name__ == '__main__':
    print(Solution().majorityElement_1([3,2,3]))
    print(Solution().majorityElement_1([2,2,1,1,1,2,2]))
    print("=====================================")