# -*- coding: utf-8 -*-
class Solution(object):
    # Runtime 22 ms / Memory 13.4 MB
    def addDigits_1(self, num):
        while num > 9:
            r = 0
            for n in str(num):
                r += int(n)
            num = r
        return num

    # Runtime 25 ms / Memory 13.4 MB
    def addDigits_2(self, num):
        if num == 0:
            return 0
        else: # python % mod => -1%9 = 8
            return 1 + (num - 1) % 9


if __name__ == '__main__':
    print(Solution().addDigits_1(38))
    print(Solution().addDigits_1(0))
    print("=====================================")
    print(Solution().addDigits_2(38))
    print(Solution().addDigits_2(0))