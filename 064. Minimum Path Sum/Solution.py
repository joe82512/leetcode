# -*- coding: utf-8 -*-
class Solution(object):
    # Runtime 175 ms / Memory 14.6 MB
    def minPathSum_1(self, grid):
        row, column = len(grid), len(grid[0])
        for r in range(row):
            for c in range(column):
                if r == c == 0:
                    grid[r][c] += 0
                elif r == 0:
                    grid[r][c] += grid[r][c-1]
                elif c == 0:
                    grid[r][c] += grid[r-1][c]
                else:
                    grid[r][c] += min(grid[r-1][c], grid[r][c-1])
        return grid[-1][-1]

    # Runtime ms / Memory MB    
    def minPathSum_2(self, grid):
        pass



if __name__ == '__main__':
    print(Solution().minPathSum_1([[1,3,1],[1,5,1],[4,2,1]]))
    print(Solution().minPathSum_1([[1,2,3],[4,5,6]]))
    print("=====================================")