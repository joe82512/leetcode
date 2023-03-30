# -*- coding: utf-8 -*-
class Solution(object):
    # Runtime 54 ms / Memory 13.7 MB
    def solveNQueens_1(self, n):
        def check(queens): #對角線判斷
            i = len(queens) - 1
            for j in range(i):
                if i - j == abs(queens[i] - queens[j]):
                    return False
            return True
        
        def dfs(queens, n, result):
            if len(queens) == n: #Tree到底建立字串
                s = "."*len(queens)
                row_index = [s[:i]+"Q"+s[i+1:] for i in queens]
                result.append(row_index)
                return
            else:
                for idx in range(n): #Tree root-(0,1,2,3)-(0,1,2,3)*4-(...)*16
                    if idx not in queens: #同位置判斷
                        queens.append(idx)
                        if check(queens):
                            dfs(queens, n, result)
                        queens.pop()
        r = []   
        dfs([], n, r)
        return r

    # Runtime ms / Memory MB
    def solveNQueens_1(self, n):
        pass