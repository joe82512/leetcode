# -*- coding: utf-8 -*-
class Solution(object):
    # Runtime 23 ms / Memory 13.5 MB
    def mergeAlternately_1(self, word1, word2):
        L = max(len(word1),len(word2))
        r = ""
        for i in range(L):
            if i < len(word1):
                r += word1[i]
            if i < len(word2):
                r += word2[i]
        return r

    # Runtime 19 ms / Memory 13.4 MB
    def mergeAlternately_2(self, word1, word2):
        ans = ""
        for a,b in zip(word1,word2):
            ans += a
            ans += b
        
        if len(word1)>len(word2):
            return ans+word1[len(word2):]
        return ans+word2[len(word1):]
