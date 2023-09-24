# -*- coding: utf-8 -*-
class Solution:
    # Runtime 346 ms / Memory 14.6 MB
    def canJump_1(self, nums):
        n = len(nums)
        position = 0
        for i in range(n):
            if (i>position): #cant goal next place
                return False
            position = max(position, i+nums[i]) #go max step
            
            if (position >= n-1):
                return True

    # Runtime 350 ms / Memory 14.2 MB    
    def canJump_2(self, nums):
        last_pos = len(nums)-1
        for i in range(len(nums)-2,-1,-1): #move forward
            if (i+nums[i]) >= last_pos: #you can move
                last_pos = i

        return last_pos == 0