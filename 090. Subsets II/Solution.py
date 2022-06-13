# -*- coding: utf-8 -*-
class Solution:
    # Runtime 23 ms / Memory 13.7 MB
    def subsetsWithDup_1(self, nums):
        nums.sort()
        result = [[]]
        for i in nums:
            # cant use append
            result += [ j+[i] for j in result if not j+[i] in result]
        return result

    # Runtime ms / Memory MB    
    def subsetsWithDup_2(self, nums):
        pass



if __name__ == '__main__':
    print(Solution().subsetsWithDup_1([1,2,2]))
    print(Solution().subsetsWithDup_1([0]))
    print("=====================================")
    print(Solution().subsetsWithDup_2([1,2,2]))
    print(Solution().subsetsWithDup_2([0]))