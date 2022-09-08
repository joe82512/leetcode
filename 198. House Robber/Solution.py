# -*- coding: utf-8 -*-
class Solution:
    # Runtime 17 ms / Memory 13.5 MB
    def rob_1(self, nums):
        '''
        F(i) = max(F(i-2)+nums[i], F(i-1))
        '''        
        a = nums[0]
        if len(nums) == 1:
            return a
        else:
            b = max(nums[0],nums[1])
            for n in nums[2:]:
                b, a = max(a+n,b), b
            return b

    # Runtime ms / Memory MB
    def rob_2(self, nums):
        pass



if __name__ == '__main__':
    print(Solution().rob_1([1,2,3,1]))
    print(Solution().rob_1([2,7,9,3,1]))
    print("=====================================")