# -*- coding: utf-8 -*-
class Solution:
    # Runtime 38 ms / Memory 13.3 MB
    def heightChecker_1(self, heights):
        expected = sorted(heights)
        not_match = 0
        for idx, value in enumerate(heights):
            if value != expected[idx]:
                not_match += 1
        return not_match

    # Runtime ms / Memory MB
    def heightChecker_2(self, heights):
        pass



if __name__ == '__main__':
    print(Solution().heightChecker_1([1,1,4,2,1,3]))
    print(Solution().heightChecker_1([5,1,2,3,4]))
    print(Solution().heightChecker_1([1,2,3,4,5]))
    print("=====================================")