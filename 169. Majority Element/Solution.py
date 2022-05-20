# -*- coding: utf-8 -*-
class Solution:
    # Runtime 176 ms / Memory 14.7 MB
    def majorityElement_1(self, nums):
        nums = sorted(nums)
        return nums[int(len(nums)/2)]

    # Runtime 136 ms / Memory 14.9 MB
    def majorityElement_2(self, nums):
        set_dict = {}
        for num in nums:
            if num in set_dict:
                set_dict[num] += 1
            else:
                set_dict[num] = 0
        major_len = len(nums)//2

        for k in set_dict:
            if set_dict[k] >= major_len:
                return k



if __name__ == '__main__':
    print(Solution().majorityElement_1([3,2,3]))
    print(Solution().majorityElement_1([2,2,1,1,1,2,2]))
    print("=====================================")
    print(Solution().majorityElement_2([3,2,3]))
    print(Solution().majorityElement_2([2,2,1,1,1,2,2]))