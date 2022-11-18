# -*- coding: utf-8 -*-
class Solution(object):
    # Runtime 128 ms / Memory 15 MB
    def minimumTotal_1(self, triangle):
        dp = [[-1] * len(triangle) for t in range(len(triangle))]
        def dfs(i, j):
            if i == len(triangle):
                return 0
            elif dp[i][j] != -1:
                return dp[i][j]
            else:    
                left = triangle[i][j] + dfs(i + 1, j)
                right = triangle[i][j] + dfs(i + 1, j + 1)
                dp[i][j] = min(left,right)
                return dp[i][j]

        return dfs(0, 0)

    # Runtime 52 ms / Memory 14.4 MB
    def minimumTotal_2(self, triangle):
        for i in range(len(triangle)-2, -1, -1): #reverse from second last
            for j in range(len(triangle[i])):
                triangle[i][j] += min(triangle[i+1][j], triangle[i+1][j+1])
        return triangle[0][0]