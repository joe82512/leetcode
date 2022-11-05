# -*- coding: utf-8 -*-
class Solution(object):
    # Runtime 19 ms / Memory 13.5 MB
    def spiralOrder_1(self, matrix):
        if matrix == []:
            return []
        else:
            row, column = len(matrix), len(matrix[0])
            res = []
            up,down,left,right = 0,row-1,0,column-1
            while True:
                for j in range(left,right+1):
                    res.append(matrix[up][j])
                up += 1
                if up > down:
                    break
                    
                for i in range(up,down+1):
                    res.append(matrix[i][right])
                right -= 1
                if right < left:
                    break
                    
                for j in range(right,left-1,-1):
                    res.append(matrix[down][j])
                down -= 1
                if up > down:
                    break
                    
                for i in range(down,up-1,-1):
                    res.append(matrix[i][left])
                left += 1
                if right < left:
                    break
            
            return res

    # Runtime 37 ms / Memory 13.4 MB    
    def spiralOrder_2(self, matrix):
        result = []
        while matrix:
            result += matrix.pop(0)
            try:
                matrix = self.rotate(matrix)
            except:
                break
        return result

    def rotate(self, matrix):
        (x,y) = (len(matrix[0]),len(matrix))
        matrix[:] = [ [matrix[j][i] for j in range(y)] for i in range(x)]
        matrix.reverse()
        return matrix



if __name__ == '__main__':
    print(Solution().spiralOrder_1([[1,2,3],[4,5,6],[7,8,9]]))
    print(Solution().spiralOrder_1([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))
    print("=====================================")
    print(Solution().spiralOrder_2([[1,2,3],[4,5,6],[7,8,9]]))
    print(Solution().spiralOrder_2([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))