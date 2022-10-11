# -*- coding: utf-8 -*-
class Solution:
    # Runtime 32 ms / Memory 13.4 MB
    def hammingWeight_1(self, n):
        return bin(n).count('1')

    # Runtime 32 ms / Memory 13.6 MB
    def hammingWeight_2(self, n):
        res = 0
        while n:
            res += n & 1 # n & 0001
            n >>= 1 # shift, popup last
        return res



if __name__ == '__main__':
    print(Solution().hammingWeight_1(11))
    print(Solution().hammingWeight_1(128))
    print("=====================================")
    print(Solution().hammingWeight_2(11))
    print(Solution().hammingWeight_2(128))