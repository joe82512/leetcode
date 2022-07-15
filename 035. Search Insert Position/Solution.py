# -*- coding: utf-8 -*-
class Solution:
    # Runtime 44 ms / Memory 13.9 MB
    def searchInsert_1(self, nums, target):
        nums.append(target)
        nums.sort()
        return nums.index(target)

    # Runtime 49 ms / Memory 14.3 MB
    def searchInsert_2(self, nums, target):
        for idx,num in enumerate(nums):
            if num >= target:
                return idx
        return len(nums)



if __name__ == '__main__':
    print(Solution().searchInsert_1([1,3,5,6],5))
    print(Solution().searchInsert_1([[1,3,5,6]],2))
    print(Solution().searchInsert_1([[1,3,5,6]],7))
    print("=====================================")
    print(Solution().searchInsert_2([1,3,5,6],5))
    print(Solution().searchInsert_2([[1,3,5,6]],2))
    print(Solution().searchInsert_2([[1,3,5,6]],7))