# -*- coding: utf-8 -*-
class Solution(object):
    # Runtime 15 ms / Memory 13.3 MB
    def countOdds_1(self, low, high):
        if low%2==0:
            low += 1
        if high%2==0:
            high -= 1
        return (high - low)/2 + 1

    # Runtime ms / Memory MB
    def countOdds_2(self, low, high):
        pass