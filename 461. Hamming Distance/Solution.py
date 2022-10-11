# -*- coding: utf-8 -*-
class Solution(object):
    # Runtime 34 ms / Memory 13.5 MB
    def hammingDistance_1(self, x, y):
        return bin(x^y).count('1')

    # Runtime ms / Memory MB
    def hammingDistance_2(self, x, y):
        pass



if __name__ == '__main__':
    print(Solution().hammingDistance_1(1, 4))
    print(Solution().hammingDistance_1(3, 1))
    print("=====================================")