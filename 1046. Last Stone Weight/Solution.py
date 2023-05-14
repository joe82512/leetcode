# -*- coding: utf-8 -*-
class Solution(object):
    # Runtime 20 ms / Memory 13.1 MB
    def lastStoneWeight_1(self, stones):
        stones.sort()
        while len(stones)>=2:
            y=stones.pop()
            x=stones.pop()
            if x!=y:
                stones.append(y-x)
            stones.sort()
        
        if len(stones)==1:
            return stones[0]
        else:
            return 0 

    # Runtime ms / Memory MB
    def lastStoneWeight_2(self, stones):
        pass
