# -*- coding: utf-8 -*-
class Solution(object):
    # Runtime 582 ms / Memory 13.9 MB
    def maxDistance_1(self, grid):
        queue = []
        x, y = len(grid[0]), len(grid)
        for i in range(y):
            for j in range(x):
                if grid[i][j] == 1:
                    queue.append((i,j,0))
        
        # all 1 or all 0
        if len(queue) == x*y or len(queue) == 0:
            return -1 
        
        # BFS
        directions = [(0,1),(1,0),(-1,0),(0,-1)]
        area = 1
        while queue:
            (i, j, d) = queue.pop(0)
            for dirs in directions: #4 dir
                next_i = i + dirs[0]
                next_j = j + dirs[1]
                if (y > next_i >=0) and ( x > next_j >= 0): #B.C.
                    if (grid[next_i][next_j] == 0):
                        queue.append((next_i,next_j,d+1))
                        grid[next_i][next_j] = d+1
                        area = max(area, grid[next_i][next_j])
        return area

    # Runtime 357 ms / Memory 13.8 MB
    def maxDistance_2(self, grid):
        if max(max(grid))==0 or min(min(grid))==1:
            return -1

        m = len(grid)
        dist = [[0 for x in range(m)] for y in range(m)] #dp
        boundary = 201 #max = 100+100
        
        area = 0
        for i in range(m): #forward
            for j in range(m):
                if grid[i][j]==0:
                    if i==0:
                        U = boundary
                    elif grid[i-1][j]==1:
                        U = 1
                    elif grid[i-1][j]==0:
                        U = dist[i-1][j] + 1
                
                    if j==0:
                        L = boundary
                    elif grid[i][j-1]==1:
                        L = 1
                    elif grid[i][j-1]==0:
                        L = dist[i][j-1] + 1

                    dist[i][j] = min(U,L)
        
        for i in reversed(range(m)): #backward
            for j in reversed(range(m)):
                if grid[i][j]==0:
                    if i==m-1:
                        D = boundary
                    elif grid[i+1][j]==1:
                        D = 1
                    elif grid[i+1][j]==0:
                        D = dist[i+1][j] + 1
                
                    if j==m-1:
                        R = boundary
                    elif grid[i][j+1]==1:
                        R = 1
                    elif grid[i][j+1]==0:
                        R = dist[i][j+1] + 1

                    dist[i][j] = min(D,R,dist[i][j])
                    area = max(area, dist[i][j])
        return area