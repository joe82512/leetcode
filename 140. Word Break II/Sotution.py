# -*- coding: utf-8 -*-
class Solution(object):
    # Runtime 15 ms / Memory 13.5 MB
    def wordBreak_1(self, s, wordDict):
        table = {}
        def DFS(s):
            if s in table:
                return table[s]
            else:
                ans = []
                if s in wordDict:
                    ans.append(s)
                for r_idx in range(1, len(s)):
                    right = s[r_idx:]
                    if right in wordDict:
                        for left in DFS(s[:r_idx]):
                            ans.append(left + " " + right)
                table[s] = ans
                return table[s]
        
        r = DFS(s)
        return r

    # Runtime 12 ms / Memory 13.5 MB
    def wordBreak_2(self, s, wordDict):
        combination = []
        def DFS(idx, path):
            if idx==len(s):
                combination.append(" ".join(path))
            for i in range(len(s)):
                word = s[idx:i+1]
                if word in wordDict:
                    DFS(i+1,path+[word])
        
        DFS(0, [])
        return combination