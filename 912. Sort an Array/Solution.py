# -*- coding: utf-8 -*-
class Solution(object):
    # Runtime 1564 ms / Memory 22.1 MB
    def sortArray_1(self, nums):
        self.mergeSort(nums)
        return nums

    def mergeSort(self,nums):
        if len(nums) > 1: 
            mid = len(nums)//2
            L = nums[:mid] 
            R = nums[mid:] 

            self.mergeSort(L)
            self.mergeSort(R)

            i = j = k = 0

            while i < len(L) and j < len(R): 
                if L[i] < R[j]: 
                    nums[k] = L[i] 
                    i+=1
                else: 
                    nums[k] = R[j] 
                    j+=1
                k+=1
 
            while i < len(L): 
                nums[k] = L[i] 
                i+=1
                k+=1

            while j < len(R): 
                nums[k] = R[j] 
                j+=1
                k+=1

    # Runtime 705 ms / Memory 25.7 MB
    def sortArray_2(self, nums):
        c_len = 50000+1-(-50000)
        count = [0 for i in range(c_len)]
        result = []
        for n in nums:
            count[n+50000] += 1

        for i in range(c_len):
            if count[i] != 0:
                while count[i]!=0:
                    count[i] -= 1 #duplicate value
                    result.append(i-50000)
            else:
                continue
        return result