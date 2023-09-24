# -*- coding: utf-8 -*-
class Solution:
    # Runtime 574 ms / Memory 15 MB
    def replaceElements_1(self, arr):
        temp = -1
        for i in range(len(arr)-1,-1,-1):
            arr[i],temp = temp,max(arr[i],temp)

        return arr

    # Runtime ms / Memory MB    
    def eplaceElements_2(self, s):
        pass