# -*- coding: utf-8 -*-
class Solution:
    # Runtime 127 ms / Memory 13.4 MB
    def isToeplitzMatrix_1(self, matrix):
        row, column = len(matrix),len(matrix[0])
        for r in range(row-1):
            for c in range(column-1):
                if matrix[r][c] != matrix[r+1][c+1]:
                    return False
        return True

    # Runtime ms / Memory MB
    def isToeplitzMatrix_2(self, matrix):
        pass