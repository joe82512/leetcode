# -*- coding: utf-8 -*-
class Solution:
    # Runtime 492 ms / Memory 23.9 MB
    def containsDuplicate_1(self, nums):
        return len(set(nums)) != len(nums)

    # Runtime  / Memory 
    def containsDuplicate_2(self, nums):
        pass



if __name__ == '__main__':
    print(Solution().containsDuplicate_1([1,2,3,1]))
    print(Solution().containsDuplicate_1([1,2,3,4]))
    print(Solution().containsDuplicate_1([1,1,1,3,3,4,3,2,4,2]))
    print("=====================================")