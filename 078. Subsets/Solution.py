# -*- coding: utf-8 -*-
class Solution:
    # Runtime 30 ms / Memory 13.5 MB
    def subsets_1(self, nums):
        result = [[]]
        for i in nums:
            # cant use append
            result += [ j+[i] for j in result]
        return result

    # Runtime 27 ms / Memory 13.6 MB    
    def subsets_2(self, nums):
        if len(nums)==1:
            return [[],nums]
        result = []
        self.DFS(nums, [], result)
        return result
    
    def DFS(self, nums, path, result):
        result.append(path)
        for i in range(len(nums)):
            self.DFS(nums[i+1:], path+[nums[i]], result) 



if __name__ == '__main__':
    print(Solution().subsets_1([1,2,3]))
    print(Solution().subsets_1([0]))
    print("=====================================")
    print(Solution().subsets_2([1,2,3]))
    print(Solution().subsets_2([0]))