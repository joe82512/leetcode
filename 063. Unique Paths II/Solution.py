# -*- coding: utf-8 -*-
class Solution:
    # Runtime 18 ms / Memory 13.2 MB
    def uniquePathsWithObstacles_1(self, obstacleGrid):
        row = len(obstacleGrid)-1
        col = len(obstacleGrid[0])-1
        grid = [ [0 for j in range(col+1)] for i in range(row+1) ]
        # case : [[1]]
        if (obstacleGrid[0][0]==1):
            return 0
        grid[0][0] = 1
        queue = [(0,0)]

        while (queue):
            (i,j) = queue.pop(0)
            if ((i,j)==(row,col)):
                return grid[-1][-1]
            if (i<row):
                # next step : no collision and no visit
                if (obstacleGrid[i+1][j]==0 and grid[i+1][j]==0):
                    queue.append((i+1,j))
                grid[i+1][j] += grid[i][j]
            if (j<col):
                if (obstacleGrid[i][j+1]==0 and grid[i][j+1]==0):
                    queue.append((i,j+1))
                grid[i][j+1] += grid[i][j]
        
        return 0

    # Runtime 21 ms / Memory 13.2 MB    
    def uniquePathsWithObstacles_2(self, obstacleGrid):
        row = len(obstacleGrid)
        col = len(obstacleGrid[0])
        dp = [ [0]*col for _ in range(row)]
        
        if (obstacleGrid[0][0]==0):
            dp[0][0] = 1
        else:
            dp[0][0] = 0

        for i in range(row):
            for j in range(col):
                if (obstacleGrid[i][j]==1):
                    dp[i][j] = 0 #if stuck , avoid path
                else:
                    if (i>0): #i=0 Boundary
                        dp[i][j] = dp[i][j] + dp[i-1][j]
                    if (j>0): #j=0 Boundary
                        dp[i][j] = dp[i][j] + dp[i][j-1]
        
        return dp[-1][-1]