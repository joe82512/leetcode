# -*- coding: utf-8 -*-
class Solution(object):
    # Runtime 550 ms / Memory 15 MB
    def numEnclaves_1(self, grid):
        queue = []
        r = 0
        x,y = len(grid[0]),len(grid)
        for i in range(y):
            for j in range(x):
                r = r + grid[i][j]
                if (i==0) or (i==y-1):
                    queue.append((i,j))
                elif (j==0) or (j==x-1):
                    queue.append((i,j))

        while queue:
            (i,j) = queue.pop(0) #queue or stack
            if (y>i>=0) and (x>j>=0) and grid[i][j] == 1:
                grid[i][j] = 0
                r -= 1
                queue.append((i+1,j))
                queue.append((i-1,j))
                queue.append((i,j+1))
                queue.append((i,j-1))
        
        return r

    # Runtime ms / Memory MB
    def numEnclaves_2(self, grid):
        pass