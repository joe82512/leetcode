# -*- coding: utf-8 -*-
class Solution:
    # Runtime 35 ms / Memory 13.7 MB
    def reverseBits_1(self, n):
        bin_n = bin(n)
        len_zero = 32 - (len(bin_n)-2)
        full_n = ''.join(['0' for i in range(len_zero)]) + bin_n[2:]
        return int(full_n[::-1],2)

    # Runtime 49 ms / Memory 13.3 MB
    def reverseBits_2(self, n):
        out = 0
        for i in range(32):
            if (n%2==1):
                out = (out << 1) + 1
            else:
                out = out << 1
            n = n >> 1
        return out