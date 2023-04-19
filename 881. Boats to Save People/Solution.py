# -*- coding: utf-8 -*-
class Solution(object):
    # Runtime 366 ms / Memory 18.6 MB
    def numRescueBoats_1(self, people, limit):
        people.sort()
        L,R = 0,len(people)-1
        boats = 0
        while (L<=R):
            if people[L]+people[R] <= limit:
                L = L+1
                R = R-1
            else:
                R = R-1
            boats += 1
        return boats+1
    
    # Runtime ms / Memory MB
    def numRescueBoats_2(self, people, limit):
        pass