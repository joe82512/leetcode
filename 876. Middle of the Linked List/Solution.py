# -*- coding: utf-8 -*-
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    # Runtime 28 ms / Memory 13.4 MB
    def middleNode_1(self, head):
        s2 = s1 = head
        while s2 and s2.next:
            s2 = s2.next.next
            s1 = s1.next
        return s1

    # Runtime 23 ms / Memory 13.6 MB
    def middleNode_2(self, head):
        output = head
        count = 1
        while head.next:
            head = head.next
            count += 1

        looptime = count//2
        for i in range(looptime):
            output = output.next
        return output