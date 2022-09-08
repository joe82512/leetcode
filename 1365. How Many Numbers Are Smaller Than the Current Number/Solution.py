# -*- coding: utf-8 -*-
class Solution:
    # Runtime 47 ms / Memory 13.2 MB
    def smallerNumbersThanCurrent_1(self, nums):
        counters, c = {}, 0 # count duplicate
        counters_sum, c_sum = {}, 0 # count total
        for sn in sorted(nums):
            if sn in counters:
                counters[sn] += 1 #duplicate
            else:
                counters[sn] = 1 #first
            c_sum += 1
            counters_sum[sn] = c_sum #sum
            
        return [(counters_sum[n]-counters[n]) for n in nums]

    # Runtime 47 ms / Memory 13.7 MB
    def smallerNumbersThanCurrent_2(self, nums):
        # same as method 1
        sr_nums = sorted(nums)            
        return [sr_nums.index(n) for n in nums]



if __name__ == '__main__':
    print(Solution().smallerNumbersThanCurrent_1([8,1,2,2,3]))
    print(Solution().smallerNumbersThanCurrent_1([6,5,4,8]))
    print(Solution().smallerNumbersThanCurrent_1([7,7,7,7]))
    print("=====================================")
    print(Solution().smallerNumbersThanCurrent_2([8,1,2,2,3]))
    print(Solution().smallerNumbersThanCurrent_2([6,5,4,8]))
    print(Solution().smallerNumbersThanCurrent_2([7,7,7,7]))