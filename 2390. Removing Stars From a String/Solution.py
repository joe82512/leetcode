# -*- coding: utf-8 -*-
class Solution(object):
    # Runtime 306 ms / Memory 16.7 MB
    def removeStars_1(self, s):
        stack = []
        for v in s:
            if v == "*":
                stack.pop()
            else:
                stack.append(v)
        return ("").join(stack)

    # Runtime ms / Memory MB
    def removeStars_2(self, s):
        pass
