# -*- coding: utf-8 -*-
class Solution:
    # Runtime 26 ms / Memory 14.5 MB
    def isIsomorphic_1(self, s, t):
        if (len(s)!=len(t)):
            return False
        st_map = {}
        for i in range(len(s)):
            if s[i] in st_map:
                if (st_map[s[i]]!=t[i]):
                    return False
            else:
                st_map[s[i]] = t[i]
        
        return len(st_map) == len(set(st_map.values()))

    # Runtime 31 ms / Memory 14 MB    
    def isIsomorphic_2(self, s, t):
        return [s.find(i) for i in s] == [t.find(j) for j in t]