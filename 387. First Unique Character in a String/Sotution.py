# -*- coding: utf-8 -*-
class Solution(object):
    # Runtime 72 ms / Memory 13.5 MB
    def firstUniqChar_1(self, s):
        cnt = {}
        for c in s:
            if c in cnt:
                cnt[c] += 1
            else:
                cnt[c] = 1
        
        for c in s:
            if cnt[c] == 1 :
                return s.index(c)
        
        return -1

    # Runtime 33 ms / Memory 13.7 MB
    def firstUniqChar_2(self, s):
        idx = []
        for c in set(s):
            cnt = s.count(c)
            if cnt==1:
                idx.append(s.index(c)) #get 1 index
        
        if idx:
            return min(idx)
        else:
            return -1