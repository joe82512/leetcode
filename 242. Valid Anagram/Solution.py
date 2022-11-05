# -*- coding: utf-8 -*-
class Solution(object):
    # Runtime 116 ms / Memory 14.6 MB
    def isAnagram_1(self, s, t):
        return sorted(s) == sorted(t)

    # Runtime ms / Memory MB
    def isAnagram_2(self, num):
        pass