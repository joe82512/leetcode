# -*- coding: utf-8 -*-
class Solution:
    # Runtime 48 ms / Memory 14.4 MB
    def transpose_1(self, matrix):
        (x,y) = (len(matrix[0]),len(matrix))
        return [ [matrix[j][i] for j in range(y)] for i in range(x)]

    # Runtime ms / Memory MB
    def transpose_2(self, matrix):
        pass



if __name__ == '__main__':
    print(Solution().transpose_1([[1,2,3],[4,5,6],[7,8,9]]))
    print(Solution().transpose_1([[1,4,7],[2,5,8],[3,6,9]]))
    print("=====================================")