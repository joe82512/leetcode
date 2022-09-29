# -*- coding: utf-8 -*-
class Solution(object):
    # Runtime 116 ms / Memory 15.6 MB
    def missingNumber_1(self, nums):
        r = set([i for i in range(len(nums)+1)])-set(nums)
        return list(r)[0]

    # Runtime 24 ms / Memory 13.1 MB
    def missingNumber_2(self, nums):
        pass


if __name__ == '__main__':
    print(Solution().missingNumber_1([3,0,1]))
    print(Solution().missingNumber_1([0,1]))
    print(Solution().missingNumber_1([9,6,4,2,3,5,7,0,1]))
    print("=====================================")   