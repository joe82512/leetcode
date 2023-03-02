# -*- coding: utf-8 -*-
class Solution(object):
    # Runtime 149 ms / Memory 21.2 MB
    def reverseString_1(self, s):
        for i in range(int(len(s)/2)):
            s[i], s[-i - 1] = s[-i - 1], s[i]

    # Runtime 157 ms / Memory 21.1 MB
    def reverseString_2(self, s):
        s.reverse()