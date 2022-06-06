# -*- coding: utf-8 -*-
class Solution:
    # Runtime 56 ms / Memory 13.5 MB
    def removeElement_1(self, nums, val):
        n = nums.count(val)
        k = len(nums) - n
        for i in range(n):
            nums.remove(val)
        return k

    # Runtime  / Memory 
    def removeElement_2(self, nums, val):
        pass



if __name__ == '__main__':
    print(Solution().removeElement_1([3,2,2,3],3))
    print(Solution().removeElement_1([0,1,2,2,3,0,4,2],2))
    print("=====================================")