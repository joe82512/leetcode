# -*- coding: utf-8 -*-

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    # Runtime 14 ms / Memory 13.4 MB
    def swapPairs(self, head):
        if not(head and head.next):
            return head 
        
        newHead = head.next
        head.next, newHead.next = self.swapPairs(head.next.next), head

        return newHead
    #https://leetcode.com/problems/swap-nodes-in-pairs/solutions/1774708/c-visual-image-how-links-change-explained-every-step-commented-code/
    

    # Runtime 11 ms / Memory 13.4 MB
    def swapPairs_2(self, head):
        dummy = ListNode()
        prev, curr = dummy, head

        if not (head and head.next):
            return head

        while (curr and curr.next):
            prev.next = curr.next
            curr.next = prev.next.next
            prev.next.next = curr

            prev = curr
            curr = curr.next
        
        return dummy.next
    #https://leetcode.com/problems/swap-nodes-in-pairs/solutions/1775033/swapping-nodes-not-just-the-values-visual-explanation-well-explained-c/