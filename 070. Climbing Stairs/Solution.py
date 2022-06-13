# -*- coding: utf-8 -*-
from math import factorial as fa

class Solution:
    # Runtime 34 ms / Memory 13.3 MB
    def combination(self,m,n): #排列組合Cm取n
        return fa(m)//(fa(n)*fa(m-n))
    
    def climbStairs_1(self, n):
        result = 0
        for i in range(n):
            if n-i >= i:
                result += self.combination(n-i,i) # C(n-i)取i
            else: # m >= n
                break
        return result

    # Runtime 24 ms / Memory 13.2 MB
    def climbStairs_2(self, n):
        #費氏數列, 下一階可從前兩階或前一階跨步
        a0,a1 = 0,1
        for i in range(n):
            a1,a0 = a1+a0,a1
        return a1



if __name__ == '__main__':
    print(Solution().climbStairs_1(2))
    print(Solution().climbStairs_1(3))
    print("=====================================")
    print(Solution().climbStairs_2(2))
    print(Solution().climbStairs_2(3))