# -*- coding: utf-8 -*-
class Solution:
    # Runtime 7 ms / Memory 13.5 MB
    def fib_1(self, n):
        a = 0
        b = 1
        if n == 0:
            return a
        elif n == 1:
            return b
        else:
            for i in range(n-1):
                b, a = a+b, b
            return b

    # Runtime ms / Memory MB
    def fib_2(self, n):
        pass



if __name__ == '__main__':
    print(Solution().fib_1(2))
    print(Solution().fib_1(3))
    print(Solution().fib_1(4))
    print("=====================================")