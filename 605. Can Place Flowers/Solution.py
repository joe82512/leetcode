# -*- coding: utf-8 -*-
class Solution(object):
    # Runtime 125 ms / Memory 13.7 MB
    def canPlaceFlowers_1(self, flowerbed, n):
        if not flowerbed:
            return False
        #else
        if flowerbed[0]==0:      
            cnt = 1 #起頭為0001 -> 2
        else:
            cnt = 0
        s = 0
        for fb in flowerbed:
            if fb == 0:
                cnt += 1 #連續0
            else:
                t = (cnt-1)//2 #3個0變1個,4個0變1個,5個0變2個
                # [10001] => [10101]
                # [100001] => [101001] or [100101]
                # [1000001] => [1010101]
                if t<1:
                    t = 0
                s = s + t
                cnt = 0
        if flowerbed[-1]==0:
            s = s + cnt//2 #最後為0
        return s>=n
    
    # Runtime 123 ms / Memory 14 MB
    def canPlaceFlowers_2(self, flowerbed, n):
        cnt = 0
        for i in range(len(flowerbed)):
            if (i==0 or flowerbed[i-1]==0) and (flowerbed[i]==0) and (i==len(flowerbed)-1 or flowerbed[i+1]==0):
                flowerbed[i] = 1
                cnt += 1
        return cnt>=n