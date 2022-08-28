# -*- coding: utf-8 -*-
class Solution:
    # Runtime 116 ms / Memory 13.9 MB
    def getConcatenation_1(self, nums):
        return nums+nums

    # Runtime ms / Memory MB
    def getConcatenation_2(self, nums):
        pass



if __name__ == '__main__':
    print(Solution().getConcatenation_1([1,2,1]))
    print(Solution().getConcatenation_1([1,3,2,1]))
    print("=====================================")
    print(Solution().getConcatenation_2([1,2,1]))
    print(Solution().getConcatenation_2([1,3,2,1]))