# -*- coding: utf-8 -*-
class Solution(object):
    # Runtime 67 ms / Memory 13.2 MB
    def isPowerOfThree_1(self, n):
        if (n < 3) and (n!=1) :
            return False
        while (n>1):
            if (n%3==0):
                n = n/3
            else:
                return False
                
        return True

    # Runtime 87 ms / Memory 13.4 MB
    def isPowerOfThree_2(self, n):
        x = 1
        while True:
            if x == n:
                return True
            elif x > n:
                return False
            x = x*3