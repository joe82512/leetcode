# -*- coding: utf-8 -*-
class Solution(object):
    # Runtime 16 ms / Memory 13.3 MB
    def numJewelsInStones_1(self, jewels, stones):
        cnt = 0
        for s in stones:
            if s in jewels:
                cnt += 1
        return cnt

    # Runtime 24 ms / Memory 13.3 MB
    def numJewelsInStones_2(self, jewels, stones):
        return sum(map(jewels.count,stones))