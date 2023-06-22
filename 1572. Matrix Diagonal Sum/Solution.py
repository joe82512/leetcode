# -*- coding: utf-8 -*-
class Solution(object):
    # Runtime 90 ms / Memory 13.3 MB
    def diagonalSum_1(self, mat):
        r = 0
        n = len(mat)
        for i in range(n):
            if (n%2==1) and (i==(n-1)/2):
                r = r + mat[i][i]
            else:
                r = r + mat[i][i] + mat[i][n-1-i]
        return r

    # Runtime ms / Memory MB
    def diagonalSum_2(self, mat):
        pass