# -*- coding: utf-8 -*-
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers_1(self, l1, l2):
        ls = root = ListNode(0)
        val = 0
        while l1 or l2 or val:
            if l1:
                val = val + l1.val
                l1 = l1.next
            if l2:
                val = val + l2.val
                l2 = l2.next
            
            ls.next = ListNode(val%10)
            ls = ls.next
            val = val//10

        return root.next

    def addTwoNumbers_2(self, l1, l2):
        pass