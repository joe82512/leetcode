# -*- coding: utf-8 -*-
class Solution(object):
    # Runtime 44 ms / Memory 15.1 MB
    def singleNumber_1(self, nums):
        ones = 0
        twos = 0
        for num in nums:
            ones = (ones ^ num) & ~twos #不成對且沒有第二次
            twos = (twos ^ num) & ~ones #出現過兩次
        return ones
    
    # https://leetcode.com/problems/single-number-ii/solutions/3714928/bit-manipulation-c-java-python-beginner-friendly/

    # Runtime 74 ms / Memory 14.8 MB
    def singleNumber_2(self, nums):
        res,one_bit,bit_sum = (0,0,0) #constant extra space

        for i in range(32): #each bit sum by idx
            bit_sum = 0
            for num in nums:
                if num < 0: #2's complement
                    num = num + 2**32
                one_bit = num >> i #get idx
                bit_sum += (one_bit&1) #get 1
            
            one_bit = bit_sum % 3 #0or1
            one_bit = one_bit << i #recover idx
            res = res | one_bit #set 1
        
        if res > 2**31-1: #2's complement
            res = res - 2**32

        return res