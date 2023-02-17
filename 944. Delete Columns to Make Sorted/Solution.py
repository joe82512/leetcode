# -*- coding: utf-8 -*-
class Solution(object):
    # Runtime 121 ms / Memory 14.6 MB
    def minDeletionSize_1(self, strs):
        r = 0
        for j in range(len(strs[0])):
            for i in range(1,len(strs)):
                if strs[i][j] < strs[i-1][j]:
                    r += 1
                    break
        return r

    # Runtime 89 ms / Memory 15.3 MB
    def minDeletionSize_2(self, strs):
        strsT = list(zip(*strs)) #Transpose
        r = 0
        for idx, string in enumerate(strsT):
            if list(string) != sorted(string):
                r = r + 1  
        return r