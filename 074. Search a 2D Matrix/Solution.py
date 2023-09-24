# -*- coding: utf-8 -*-
class Solution:
    # Runtime 21 ms / Memory 13.6 MB
    def searchMatrix_1(self, matrix, target):
        if len(matrix)==0:
            return False

        L = 0
        R = len(matrix)-1
        row = 0
        while L<=R:
            mid = int((L+R)//2)
            if matrix[mid][-1] < target:
                L = mid+1
            elif matrix[mid][0] > target:
                R = mid-1
            else:
                row = mid
                break

        L = 0
        R = len(matrix[0])-1

        while L<=R:
            mid = int((L+R)//2)
            if matrix[row][mid] < target:
                L = mid+1
            elif matrix[row][mid] > target:
                R = mid-1
            else:
                return True #find
        return False #not find

    # Runtime 25 ms / Memory 13.6 MB    
    def searchMatrix_2(self, matrix, target):
        if not matrix or not matrix[0]:
            return False
        
        m, n = len(matrix), len(matrix[0])
        left, right = 0, m * n - 1
        
        while left <= right:
            mid = left + (right - left) // 2
            row, col = divmod(mid, n)
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return False