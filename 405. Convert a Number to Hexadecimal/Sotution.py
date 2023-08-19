# -*- coding: utf-8 -*-
class Solution(object):
    # Runtime 17 ms / Memory 13.2 MB
    def toHex_1(self, num):
        if num == 0:
            return '0'
        
        if num < 0:
            num = num + 2**32

        hex_map = '0123456789abcdef'
        result = ''
        while num > 0:
            num, idx = divmod(num,16)
            result += hex_map[idx]

        return result[::-1]

    # Runtime 10 ms / Memory 13.1 MB
    def firstUniqChar_2(self, s):
        hex_map = '0123456789abcdef'
        result = ''
        
        for i in range(8): #8*4bits
            idx = num & 15 #just care last 4-bits
            c = hex_map[idx]
            result = c + result
            num = num >> 4 #15 = 1111 (4-bits)
        
        return result.lstrip('0') #not regular