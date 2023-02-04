# -*- coding: utf-8 -*-
from collections import defaultdict
class Solution(object):
    # Runtime 15 ms / Memory 13.8 MB
    def wordPattern_1(self, pattern, s):
        list_str = s.split(" ")
        result = {}

        if len(list_str) != len(pattern):
            return False

        for idx, p in enumerate(pattern):
            if p in result:
                if result[p] != list_str[idx]:
                    return False
            else:
                result[p] = list_str[idx]
        
        if len(set(result.values())) != len(result.values()):
            return False

        return True

    # Runtime 22 ms / Memory 13.3 MB
    def wordPattern_2(self, pattern, s):
        patDict = defaultdict(str)
        for pat, val in zip(pattern, s.split(" ") ):
            if val not in patDict.values():
                patDict[pat] = val

        newS = []
        for pat in pattern:
            newS.append(patDict[pat])
        newS = " ".join(newS)

        return newS == s