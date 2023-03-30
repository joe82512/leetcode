# -*- coding: utf-8 -*-
from collections import defaultdict
class Solution(object):
    # Runtime 779 ms / Memory 26.8 MB
    def minimumRounds_1(self, tasks):
        cnt = defaultdict(int)
        for key in tasks:
            cnt[key] += 1

        r = 0
        for c in cnt.values():
            if c == 1:
                return -1
            if c%3==0:
                r += c/3
            else:
                r += c/3 + 1
        return r 

    # Runtime 791 ms / Memory 26.8 MB
    def minimumRounds_2(self, tasks):
        cnt = defaultdict(int)
        for key in tasks:
            cnt[key] += 1

        r = 0
        for c in cnt.values():
            if c == 1:
                return -1
            r += (c+2)/3
        return r 