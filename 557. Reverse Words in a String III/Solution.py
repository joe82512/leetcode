# -*- coding: utf-8 -*-
class Solution(object):
    # Runtime 17 ms / Memory 14.5 MB
    def reverseWords_1(self, s):
        return ' '.join([i[::-1] for i in s.split()])

    # Runtime 617 ms / Memory 14 MB
    def reverseWords_2(self, s):
        result = ""
        stack = []
        for c in s:
            if c == " ":
                while (stack):
                    result += stack.pop()
                result += " "
            else:
                stack.append(c)
        #last stack
        while (stack):
            result += stack.pop()

        return result