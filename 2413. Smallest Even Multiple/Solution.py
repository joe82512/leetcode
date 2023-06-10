# -*- coding: utf-8 -*-
class Solution(object):
    # Runtime 18 ms / Memory 13.3 MB
    def smallestEvenMultiple_1(self, n):
        if n%2!=0:
            return n*2
        else:
            return n

    # Runtime ms / Memory MB
    def smallestEvenMultiple_2(self, n):
        pass