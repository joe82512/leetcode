# -*- coding: utf-8 -*-
class Solution(object):
    # Runtime 27 ms / Memory 13.6 MB
    def maximum69Number_1 (self, num):
        r = len(str(num))
        for i,n in enumerate(str(num)):
            if n == "6":
                r = i
                break
        
        result = num + int(3 * 10**(len(str(num))-1 - r))
        return result

    # Runtime 17 ms / Memory 13.8 MB
    def maximum69Number_2 (self, num):
        num = str(num)
        return int(num.replace('6','9',1))