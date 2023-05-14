# -*- coding: utf-8 -*-
class Solution(object):
    # Runtime 991 ms / Memory 28.4 MB
    def longestPalindromeSubseq_1(self, s):
        n = len(s)
        dp = [[0]*n for _ in range(n)]
        
        for i in range(n-1, -1, -1):
            dp[i][i] = 1
            for j in range(i+1, n):
                if s[i] == s[j]:
                    dp[i][j] = 2 + dp[i+1][j-1]
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1])
                    
        return dp[0][n-1]

        # ref: https://blog.csdn.net/fuxuemingzhu/article/details/79572746

    # Runtime 1002 ms / Memory 13.5 MB
    def longestPalindromeSubseq_2(self, s):
        n = len(s)
        dp = [1]*n
        r = 0
        
        for i in range(n-1, -1, -1):
            x = 0
            for j in range(i+1, n):
                temp = dp[j]
                if s[i] == s[j]:
                    dp[j] = 2 + x
                x = max(x,temp)
        
        return max(dp)
