# -*- coding: utf-8 -*-
from collections import defaultdict
class Solution(object):
    # Runtime 855 ms / Memory 20.6 MB
    def canCompleteCircuit_1(self, gas, cost):
        total,temp,station = 0,0,0
        for i in range(len(gas)):
            t = gas[i] - cost[i]
            total += t
            temp += t
            if temp < 0:
                temp = 0
                station = i+1
        
        if total >= 0:
            return station
        else:
            return -1

    # Runtime 814 ms / Memory 19.5 MB
    def canCompleteCircuit_2(self, gas, cost):
        if sum(gas) < sum(cost):
            return -1
        temp,station = 0,0
        for i in range(len(gas)):
            t = gas[i] - cost[i]
            temp += t
            if temp < 0:
                temp = 0
                station = i+1
        return station