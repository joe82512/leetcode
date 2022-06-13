# -*- coding: utf-8 -*-
class Solution:
    # Runtime 55 ms / Memory 13.4 MB
    def isPalindrome_1(self, x):
        if x < 0:
            return False
        else:
            x = str(x)
            return x == x[::-1]

    # Runtime  / Memory 
    def isPalindrome_2(self, x):
        pass



if __name__ == '__main__':
    print(Solution().isPalindrome_1(121))
    print(Solution().isPalindrome_1(-121))
    print(Solution().isPalindrome_1(10))
    print("=====================================")