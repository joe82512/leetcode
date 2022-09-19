# -*- coding: utf-8 -*-
class Solution:
    # Runtime 32 ms / Memory 14.2 MB
    def isSubsequence_1(self, s, t):
        s = list(s)
        t = list(t)
        if len(s) > len(t):
            return False
        elif len(s) == 0:
            return True
        else:
            c = 0
            for i in range(len(t)):
                if (c <= len(s)-1):
                    if s[c] == t[i]:
                        c += 1
            return c == len(s)

    # Runtime 25 ms / Memory 13.4 MB
    def isSubsequence_2(self, s, t):
        for sub_t in t:
            if (sub_t in s) and (sub_t==s[0]):
                s = s[1:]
        return s==''



if __name__ == '__main__':
    print(Solution().isSubsequence_1("abc","ahbgdc"))
    print(Solution().isSubsequence_1("axc","ahbgdc"))
    print("=====================================")
    print(Solution().isSubsequence_2("abc","ahbgdc"))
    print(Solution().isSubsequence_2("axc","ahbgdc"))