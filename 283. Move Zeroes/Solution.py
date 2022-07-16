# -*- coding: utf-8 -*-
class Solution:
    # Runtime 211 ms / Memory 14.8 MB
    def moveZeroes_1(self, nums):
        i = 0
        for j in range(len(nums)):
            if nums[j] != 0:
                nums[j],nums[i]=nums[i],nums[j]
                i+=1

    # Runtime 227 ms / Memory 14.7 MB
    def moveZeroes_2(self, nums):
        shift = 0
        for i in range(len(nums)):
            if nums[i-shift] == 0:
                nums.pop(i-shift)
                shift += 1
        nums += [0]*shift



if __name__ == '__main__':
    print(Solution().moveZeroes_1([0,1,0,3,12]))
    print(Solution().moveZeroes_1([0]))
    print("=====================================")
    print(Solution().moveZeroes_2([0,1,0,3,12]))
    print(Solution().moveZeroes_2([0]))