# -*- coding: utf-8 -*-
class Solution:
    # Runtime 22 ms / Memory 13.5 MB
    def findTheDifference_1(self, s, t):
        r = 0
        for i in s+t:
            r ^= ord(i)
        return chr(r)

    # Runtime  / Memory 
    def findTheDifference_2(self, s, t):
        pass



if __name__ == '__main__':
    print(Solution().findTheDifference_1("abcd","abcde"))
    print(Solution().findTheDifference_1("","y"))
    print("=====================================")