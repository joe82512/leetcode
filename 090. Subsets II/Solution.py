# -*- coding: utf-8 -*-
class Solution:
    # Runtime 23 ms / Memory 13.7 MB
    def subsetsWithDup_1(self, nums):
        nums.sort()
        result = [[]]
        for i in nums:
            # cant use append
            result += [ j+[i] for j in result if not j+[i] in result]
        return result

    # Runtime 47 ms / Memory 13.7 MB    
    def subsetsWithDup_2(self, nums):
        if len(nums)==1:
            return [[],nums]
        nums.sort()
        result = []
        self.DFS(nums, [], result)
        return result
    
    def DFS(self, nums, path, result):
        result.append(path)
        for i in range(len(nums)):
            if i >0 and nums[i]==nums[i-1]:
                continue
            self.DFS(nums[i+1:], path+[nums[i]], result) 



if __name__ == '__main__':
    print(Solution().subsetsWithDup_1([1,2,2]))
    print(Solution().subsetsWithDup_1([0]))
    print("=====================================")
    print(Solution().subsetsWithDup_2([1,2,2]))
    print(Solution().subsetsWithDup_2([0]))