# -*- coding: utf-8 -*-
class Solution(object):
    # Runtime 1196 ms / Memory 28.3 MB
    def dailyTemperatures_1(self, temperatures):
        stack = []
        res = [0]*len(temperatures)
        
        for i,t in enumerate(temperatures):
            while len(stack) > 0:
                lastTuple = stack[-1]
                if lastTuple[0] < t:
                    res[lastTuple[1]] = i - lastTuple[1]
                    stack.pop()
                else:
                    break
            stack.append((t, i))
        return res

    # Runtime 2194 ms / Memory 27 MB
    def dailyTemperatures_2(self, temperatures):
        arr = [-1]*71 #30-100
        res = [0]*len(temperatures)
        
        for i in range(len(temperatures)-1,-1,-1): #reverse
            t = temperatures[i]
            j = [x for x in arr[t-30+1:] if x > -1]
            if len(j)==0:
                res[i] = 0
            else:
                res[i] = min(j)-i
            arr[t-30] = i
        return res