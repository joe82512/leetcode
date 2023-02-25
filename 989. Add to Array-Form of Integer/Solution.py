# -*- coding: utf-8 -*-
class Solution(object):
    # Runtime 287 ms / Memory 14.2 MB
    def addToArrayForm_1(self, num, k):
        num = "".join(str(num[i]) for i in range(len(num)))
        return [int(s) for s in str(int(num)+k)]

    # Runtime 226 ms / Memory 14 MB
    def addToArrayForm_2(self, num, k):
        idx = len(num)-1
        carry = 0
        while (idx>=0) or (k>0):
            k_num = k%10
            k = k/10
            if (idx>=0): #num >= k
                add = num[idx] + k_num + carry
                num[idx] = add%10
            else: #num < k
                add = k_num + carry
                num = [add%10] + num
            carry = add/10
            idx = idx - 1
        if (carry!=0): #overflow
            num = [carry] + num
        return num