# -*- coding: utf-8 -*-
class Solution(object):
    # Runtime 78 ms / Memory 14.6 MB
    def searchRange_1(self, nums, target):
        result = [-1,-1]
        for idx, value in enumerate(nums):
            if (value==target) & (result[0]==-1):
                result[0] = idx
            elif (value==target) & (result[0]!=-1) :
                result[1] = idx
        if result[1]==-1:
            result[1] = result[0]
        return result

    # Runtime 168 ms / Memory 14.5 MB
    def searchRange_2(self, nums, target):
        result = [-1,-1]
        if target in nums:
            result[0] = nums.index(target)
            result[1] = len(nums)-1 -  nums[::-1].index(target)
        return result