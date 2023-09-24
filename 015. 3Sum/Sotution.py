# -*- coding: utf-8 -*-
class Solution(object):
    # Runtime 1830 ms / Memory 213.1 MB
    def threeSum_1(self, nums):
        nums.sort()
        output = []
        for i in range(len(nums)):
            j = i + 1
            k = len(nums) - 1
            while j < k:
                sum_num = nums[i]+nums[j]+nums[k]
                if sum_num== 0:
                    output.append((nums[i], nums[j], nums[k]))
                    j += 1
                    k -= 1
                elif sum_num < 0:
                    j += 1
                else:
                    k -= 1

        return set(output)

    # Runtime 684 ms / Memory 16.61 MB
    def threeSum_2(self, nums):
        nums.sort()
        output = []
        for i in range(len(nums)):
            # all zero: i>0
            if (i > 0) and (nums[i]==nums[i-1]):
                continue
            # early break
            if nums[i] > 0:
                break
            j = i + 1
            k = len(nums) - 1
            while j < k:
                sum_num = nums[i]+nums[j]+nums[k]
                if sum_num == 0:
                    output.append((nums[i], nums[j], nums[k]))
                    j += 1
                    k -= 1
                    # same j or k continue
                    while (j < k) and (nums[j]==nums[j-1]):
                        j += 1
                    while (j < k) and (nums[k]==nums[k+1]):
                        k -= 1
                elif sum_num < 0:
                    j += 1
                else:
                    k -= 1
                
        return output