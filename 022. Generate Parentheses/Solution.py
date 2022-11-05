# -*- coding: utf-8 -*-
class Solution(object):
    # Runtime 44 ms / Memory 14 MB
    def generateParenthesis_1(self, n):
        def dfs(left, right, s):
            if len(s) == n * 2:
                res.append(s)
                return 

            if left < n:
                dfs(left + 1, right, s + '(')

            if left > right:
                dfs(left, right + 1, s + ')')
        
        res = []
        dfs(0, 0, '')
        return res

    # Runtime ms / Memory MB
    def generateParenthesis_2(self, n):
        pass