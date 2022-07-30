# -*- coding: utf-8 -*-
class Solution:
    # Runtime 37 ms / Memory 13.5 MB
    def rotate_1(self, matrix):
        matrix.reverse()
        (x,y) = (len(matrix[0]),len(matrix))
        matrix[:] = [ [matrix[j][i] for j in range(y)] for i in range(x)]

    # Runtime ms / Memory MB    
    def rotate_2(self, matrix):
        pass



if __name__ == '__main__':
    print(Solution().rotate_1([[1,2,3],[4,5,6],[7,8,9]]))
    print(Solution().rotate_1([[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]))
    print("=====================================")