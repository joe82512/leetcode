# -*- coding: utf-8 -*-
from math import factorial as fc
class Solution:
    # Runtime 37 ms / Memory 13.5 MB
    def combination(self,n,m):
        return fc(n)/(fc(m)*fc(n-m))
    
    def getRow_1(self, rowIndex):
        return [self.combination(rowIndex,i) for i in range(rowIndex+1)]

    # Runtime 31 ms / Memory 13.2 MB
    def getRow_2(self, rowIndex):
        prev = [1]
        for row in range(1,rowIndex+1):
            shift_after = prev+[0]
            shift_before = [0]+prev
            '''
            [1,1,0] + [0,1,1] = [1,2,1]
            [1,2,1,0] + [0,1,2,1] = [1,3,3,1]
            '''
            prev = [(shift_after[col]+shift_before[col]) for col in range(0,len(shift_after))]
            
        return prev



if __name__ == '__main__':
    print(Solution().getRow_1(3))
    print(Solution().getRow_1(0))
    print(Solution().getRow_1(1))
    print("=====================================")
    print(Solution().getRow_2(3))
    print(Solution().getRow_2(0))
    print(Solution().getRow_2(1))