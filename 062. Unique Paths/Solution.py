# -*- coding: utf-8 -*-
from math import factorial as fa

class Solution(object):
    # Runtime 25 ms / Memory 13.4 MB
    def combination(self,m,n): #排列組合Cm取n
        return fa(m)//(fa(n)*fa(m-n))
    
    def uniquePaths_1(self, m, n):
        return self.combination(n+m-2,n-1)

    # Runtime ms / Memory MB
    def uniquePaths_2(self, m, n):
        pass



if __name__ == '__main__':
    print(Solution().uniquePaths_1(3,7))
    print(Solution().uniquePaths_1(3,2))
    print("=====================================")