# -*- coding: utf-8 -*-
class Solution(object):
    # Runtime 991 ms / Memory 13.7 MB
    def islandPerimeter_1(self, grid):
        len_row, len_column = len(grid[0]), len(grid)
        n = 0                        
        for i in range(len_column):
            for j in range(len_row):
                if grid[i][j] == 1:
                    n += 4
                    if (i != 0) and (grid[i-1][j] == 1):
                        n -= 2
                    if (j != 0) and (grid[i][j-1] == 1):
                        n -= 2
        return n

    # Runtime ms / Memory MB
    def islandPerimeter_2(self, n):
        pass



if __name__ == '__main__':
    print(Solution().islandPerimeter_1([[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]))
    print(Solution().islandPerimeter_1([[1]]))
    print(Solution().islandPerimeter_1([[1,0]]))
    print("=====================================")
    print(Solution().islandPerimeter_2([[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]))
    print(Solution().islandPerimeter_2([[1]]))
    print(Solution().islandPerimeter_2([[1,0]]))