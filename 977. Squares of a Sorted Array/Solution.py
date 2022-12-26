# -*- coding: utf-8 -*-
class Solution(object):
    # Runtime 583 ms / Memory 15.5 MB
    def sortedSquares_1(self, nums):
        r = [n**2 for n in nums]
        return sorted(r)

    # Runtime ms / Memory MB
    def sortedSquares_2(self, nums):
        pass