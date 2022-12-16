# -*- coding: utf-8 -*-
class Solution(object):
    # Runtime 35 ms / Memory 13.8 MB
    def findMin_1(self, nums):
        left, right = 0, len(nums)-1
        while (left < right):
            mid = left + (right - left)//2            
            if (nums[mid] < nums[right]):
                right = mid
            else:
                left = mid + 1
        return nums[left]

    # Runtime 24 ms / Memory 13.6 MB
    def findMin_2(self, nums):
        if (nums[0] <= nums[-1]):
            return nums[0]
        else:
            for n in nums:
                if (n < nums[0]):
                    return n