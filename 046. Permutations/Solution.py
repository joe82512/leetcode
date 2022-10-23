# -*- coding: utf-8 -*-
class Solution:
    # Runtime 28 ms / Memory 13.5 MB
    def permute_1(self, nums):
        result = [[]]
        for num in nums:
            result = [sub[:i] + [num] + sub[i:] for sub in result for i in range(len(sub)+1)]
            '''
            temp = []
            for sub in result:
                for i in range(len(sub)+1):
                    temp.append(sub[:i] + [num] + sub[i:])
                    print('sub:',sub,'; num:',num,'; concat: ',sub[:i] + [num] + sub[i:])
            result = temp
            '''
        return result

    # Runtime 53 ms / Memory 13.3 MB    
    def permute_2(self, nums):
        res = []
        self.dfs(nums, [], res)
        return res

    def dfs(self, nums, path, res):
        if not nums:
            res.append(path)
            # print(path)
            return
        for i in range(len(nums)):
            self.dfs(nums[:i]+nums[i+1:], path+[nums[i]], res)



if __name__ == '__main__':
    print(Solution().permute_1([1,2,3]))
    print(Solution().permute_1([0,1]))
    print(Solution().permute_1([1]))
    print("=====================================")
    print(Solution().permute_2([1,2,3]))
    print(Solution().permute_2([0,1]))
    print(Solution().permute_2([1]))