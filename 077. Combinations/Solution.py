# -*- coding: utf-8 -*-
from copy import deepcopy
class Solution(object):
    # Runtime 1346 ms / Memory 14.9 MB 
    def combine(self, n, k):
        def DFS(nums,res):
            if len(res) == k:
                res_list.append(res)
                return  
            else:
                for i in range(len(nums)):
                    DFS(nums[i+1:],res+[nums[i]])

        nums = [i for i in range(1,n+1)]
        res_list = []
        DFS(nums,[])
        return res_list
    # Runtime 1557 ms / Memory 15.2 MB 
    def combine_2(self, n, k):
        def DFS(idx,res):
            if len(res) == k:
                res_list.append(deepcopy(res)) #must deepcopy
                return  
            else:
                for i in range(idx,n+1):
                    res.append(i)
                    DFS(i+1,res)
                    res.pop()

        res_list = []
        DFS(1,[])
        return res_list