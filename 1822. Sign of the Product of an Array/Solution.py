# -*- coding: utf-8 -*-
class Solution(object):
    # Runtime 43 ms / Memory 13.3 MB
    def arraySign_1(self, nums):
        r = 1
        for n in nums:
            r = r*n
        
        if r==0:
            return 0
        elif r>0:
            return 1
        else:
            return -1

    # Runtime 51 ms / Memory 13.5 MB
    def arraySign_2(self, nums):
        r = 1
        for n in nums:
            if n==0:
                return 0
            elif n<0:
                r = r * -1
        
        return r