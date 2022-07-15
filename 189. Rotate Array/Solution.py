# -*- coding: utf-8 -*-
class Solution:
    # Runtime 319 ms / Memory 24.7 MB
    def rotate_1(self, nums, k):
        k = k%len(nums)
        nums[:] = nums[-k:] + nums[:-k] #must nums[:]

    # Runtime ms / Memory MB
    def rotate_2(self, nums, k):
        pass



if __name__ == '__main__':
    print(Solution().rotate_1([1,2,3,4,5,6,7],3))
    print(Solution().rotate_1([-1,-100,3,99],2))
    print("=====================================")