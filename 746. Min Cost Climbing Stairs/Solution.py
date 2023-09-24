# -*- coding: utf-8 -*-
class Solution:
    # Runtime 41 ms / Memory 13.5 MB
    def minCostClimbingStairs_1(self, cost):
        for i in range(2,len(cost)):
            cost[i] = min(cost[i-1],cost[i-2]) + cost[i]
        
        res = min(cost[-2],cost[-1])
        return res

    # Runtime ms / Memory MB    
    def minCostClimbingStairs_2(self, cost):
        pass