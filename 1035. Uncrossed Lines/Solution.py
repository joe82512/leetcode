# -*- coding: utf-8 -*-
class Solution(object):
    # Runtime 129 ms / Memory 13.8 MB
    def maxUncrossedLines_1(self, nums1, nums2):
        (m,n) = (len(nums1),len(nums2))
        #dp = dp = [[0] * (n+1)] * (m+1) #failed !
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
        for i in range(m):
            for j in range(n):
                if nums1[i]==nums2[j]:
                    dp[i+1][j+1] = dp[i][j]+1
                else:
                    dp[i+1][j+1] = max(dp[i+1][j],dp[i][j+1])

        return dp[m][n]

    # Runtime 116 ms / Memory 13.4 MB
    def maxUncrossedLines_2(self, nums1, nums2):
        if len(nums1) < len(nums2):
            nums1,nums2 = nums2,nums1 #swap
        m, n = len(nums1), len(nums2)

        dp = [0] * (n + 1)
        for i in range(1, m + 1):
            prev = 0
            for j in range(1, n + 1):
                curr = dp[j]
                if nums1[i-1] == nums2[j-1]:
                    dp[j] = prev + 1
                else:
                    dp[j] = max(dp[j-1], curr)
                prev = curr
        return dp[n]

        #same as 1143 Longest Common Subsequence
        #https://anj910.medium.com/leetcode-1035-uncrossed-lines-%E4%B8%AD%E6%96%87-83c94cc5941b