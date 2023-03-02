# -*- coding: utf-8 -*-
class Solution(object):
    # Runtime 123 ms / Memory 20.4 MB
    def singleNonDuplicate_1(self, nums):
        left, right = 0, len(nums) - 1
        while left < right:
            mid = int((left + right) / 2)
            if mid % 2 == 1: #get even
                mid -= 1
            if nums[mid] != nums[mid + 1]: #r in left
                right = mid
            else:
                left = mid + 2 #pare
        return nums[left]

    # Runtime ms / Memory MB
    def singleNonDuplicate_2(self, nums):
        pass