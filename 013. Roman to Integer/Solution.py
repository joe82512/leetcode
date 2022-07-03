# -*- coding: utf-8 -*-
class Solution:
    # Runtime 47 ms / Memory 13.5 MB
    def romanToInt_1(self, s):
        sym_dict = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        v = [sym_dict[i] for i in s]
        result = v[0]
        for i in range(1,len(v)):
            result += v[i]
            if v[i-1] < v[i]:
                result -= v[i-1]*2
        return result

    # Runtime ms / Memory MB    
    def romanToInt_2(self, s):
        pass



if __name__ == '__main__':
    print(Solution().romanToInt_1("III"))
    print(Solution().romanToInt_1("LVIII"))
    print(Solution().romanToInt_1("MCMXCIV"))
    print("=====================================")
    print(Solution().romanToInt_2("III"))
    print(Solution().romanToInt_2("LVIII"))
    print(Solution().romanToInt_2("MCMXCIV"))    