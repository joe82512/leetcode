# -*- coding: utf-8 -*-
class Solution(object):
    # Runtime 62 ms / Memory 13.4 MB
    def targetIndices_1(self, nums, target):
        nums.sort()
        return [i for i,n in enumerate(nums) if n == target]

    # Runtime ms / Memory MB
    def targetIndices_2(self, nums, target):
        pass



if __name__ == '__main__':
    print(Solution().getConcatenation_1([1,2,5,2,3],2))
    print(Solution().getConcatenation_1([1,2,5,2,3],3))
    print(Solution().getConcatenation_1([1,2,5,2,3],5))
    print("=====================================")