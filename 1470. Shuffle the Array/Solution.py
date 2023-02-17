# -*- coding: utf-8 -*-
class Solution(object):
    # Runtime 32 ms / Memory 13.8 MB
    def shuffle_1(self, nums, n):
        r = []
        for i in range(n):
            r += [nums[i],nums[i+n]]
        return r

    # Runtime ms / Memory MB
    def shuffle_2(self, nums, n):
        pass