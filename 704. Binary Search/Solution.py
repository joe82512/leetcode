# -*- coding: utf-8 -*-
class Solution(object):
    # Runtime 193 ms / Memory 14.6 MB
    def search_1(self, nums, target):
        L,R = 0,len(nums)-1
        while (L<=R):
            mid = int((L+R)/2)
            if nums[mid] > target:
                R = mid-1
            elif nums[mid] < target:
                L = mid+1
            else:
                return mid
        return -1

    # Runtime ms / Memory MB
    def search_2(self, nums, target):
        pass