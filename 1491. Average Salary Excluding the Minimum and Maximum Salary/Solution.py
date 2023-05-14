# -*- coding: utf-8 -*-
class Solution(object):
    # Runtime 11 ms / Memory 13.5 MB
    def average_1(self, salary):
        return float(sum(salary)-min(salary)-max(salary)) / (len(salary)-2)

    # Runtime 23 ms / Memory 13.3 MB
    def average_2(self, salary):
        salary.sort()
        r = 0
        for i in range(1,len(salary)-1):
            r += salary[i]

        return float(r)/(len(salary)-2)
