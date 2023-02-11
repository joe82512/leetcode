# -*- coding: utf-8 -*-
class Solution(object):
    # Runtime 34 ms / Memory 13.5 MB
    def gcdOfStrings_1(self, str1, str2):
        s = ""
        ans = ""
        for i in range(len(str1)):
            s += str1[i]
            if len(str1)%(i+1)==0 and len(str2)%(i+1)==0 and s*(len(str1)//(i+1))==str1 and s*(len(str2)//(i+1))==str2:
                ans = s
        return ans

    # Runtime 11 ms / Memory 13.8 MB
    def gcdOfStrings_2(self, str1, str2):
        if len(str1) < len(str2):
            str1, str2 = str2, str1
        
        if str1 == str2:
            return str1

        if str1[:len(str2)] != str2:
            return ""
        else:
            return self.gcdOfStrings_2(str1[len(str2):],str2)
        return ans