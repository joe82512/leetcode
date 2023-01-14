# -*- coding: utf-8 -*-
class Solution(object):
    # Runtime 230 ms / Memory 13.7 MB
    def answerQueries_1(self, nums, queries):
        nums.sort()
        res = [0 for i in range(len(queries))]
        for i,q in enumerate(queries):
            res[i] = self.helper(nums,q)        
        return res

    def helper(self,nums,q):
        listSize, listSum = 0, 0
        for n in nums:
            listSize += n
            if listSize > q:
                break
            else:
                listSum += 1
        return listSum

    # Runtime 79 ms / Memory 13.9 MB
    def answerQueries_2(self, nums, queries):
        nums.sort()
        listSize = [] #sum list
        k = 0
        for n in nums:
            k = k + n
            listSize.append(k) 
        
        res = []
        for q in queries:
            idx = bisect_right(listSize,q) #insert data
            res.append(idx)
        return res