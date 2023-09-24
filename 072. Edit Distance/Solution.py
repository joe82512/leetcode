# -*- coding: utf-8 -*-
class Solution:
    # Runtime 101 ms / Memory 16.8 MB
    def minDistance_1(self, word1, word2):
        m = len(word1)
        n = len(word2)
        # dp[i][j] := min # Of operations to convert word1[0..i) to word2[0..j)
        dp = [[0] * (n+1) for _ in range(m+1)]

        for i in range(1, m+1): #word1
            dp[i][0] = i

        for j in range(1, n+1): #word2
            dp[0][j] = j

        for i in range(1, m+1):
            for j in range(1, n+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1] #no operation
                else:
                    dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1
                                    #replace    #delete     #insert

        return dp[m][n]

    # Runtime ms / Memory MB
    def minDistance_2(self, s, t):
        pass