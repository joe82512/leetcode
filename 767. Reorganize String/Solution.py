# -*- coding: utf-8 -*-
class Solution:
    # Runtime 13 ms / Memory 13.2 MB
    def reorganizeString_1(self, s):
        heap = sorted(s, key = lambda x: (-s.count(x), x))
        n = len(s)
        res = ""

        # 數量超過一半 , 必為空
        if heap.count(heap[0]) > (n + 1) // 2:
            return res

        for i in range(n):
            if (i%2==1): # 取後半
                res += heap[(n + i) // 2]
            else: # 取前半
                res += heap[i // 2]

        return res 

    # Runtime ms / Memory MB    
    def reorganizeString_2(self, s):
        pass