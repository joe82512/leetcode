# -*- coding: utf-8 -*-
class Solution(object):
    # Runtime 291 ms / Memory 24.7 MB
    def findDisappearedNumbers(self, nums):
        std = [i+1 for i in range(len(nums))]
        result = list( set(std) - set(nums) )
        return result

    # Runtime 761 ms / Memory 23.1 MB
    def findDisappearedNumbers_2(self, nums):
        s = set(nums)
        return [i for i in range(1, len(nums)+1) if i not in s]