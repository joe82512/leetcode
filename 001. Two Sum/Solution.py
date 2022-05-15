# -*- coding: utf-8 -*-
class Solution:
    # Runtime 3610 ms / Memory 14.4 MB
    def twoSum_1(self, nums, target):
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]

    # Runtime 84 ms / Memory 14.2 MB
    def twoSum_2(self, nums, target):
        hash_map = {} # y_value:x_index, x+y=target
        for idx, val in enumerate(nums):
            if val not in hash_map:
                hash_map[target-val] = idx
            else:
                return [hash_map[val],idx]



if __name__ == '__main__':
    print(Solution().twoSum_1([2,7,11,15],9))
    print(Solution().twoSum_1([3,2,4],6))
    print(Solution().twoSum_1([3,3],6))
    print("=====================================")
    print(Solution().twoSum_2([2,7,11,15],9))
    print(Solution().twoSum_2([3,2,4],6))
    print(Solution().twoSum_2([3,3],6))