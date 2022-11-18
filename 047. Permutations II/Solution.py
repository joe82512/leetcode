# -*- coding: utf-8 -*-
class Solution(object):
    # Runtime 1722 ms / Memory 13.8 MB
    def permuteUnique_1(self, nums):
        res = []
        self.dfs(nums, [], res)
        return res

    def dfs(self, nums, path, res):
        if not nums:
            if path not in res:
                res.append(path)
            return
        for i in range(len(nums)):
            self.dfs(nums[:i]+nums[i+1:], path+[nums[i]], res)

    # Runtime 36 ms / Memory 13.8 MB
    def permuteUnique_2(self, nums):
        nums.sort()
        res = []
        self.dfs2(nums, [], res)
        return res

    def dfs2(self, nums, path, res):
        if not nums:
            res.append(path)
            return
        for i in range(len(nums)):
            if i>0 and nums[i]==nums[i-1]:
                continue
            self.dfs2(nums[:i]+nums[i+1:], path+[nums[i]], res)