# -*- coding: utf-8 -*-

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # Runtime 20 ms / Memory 12.9 MB
    def rotateRight_1(self, head, k):
        # empty data
        if not head or not head.next:
            return head

        # create array
        vals = []
        a = head
        while a:
            vals.append(a.val)
            a = a.next
        step = k % len(vals)
        
        # return
        if step == 0:
            return head

        # rotate array -> linked-list
        vals = vals[-step:] + vals[:-step]
        root = temp = ListNode(None)
        for v in vals:
            temp.next = ListNode(v)
            temp = temp.next
        
        return root.next

    # Runtime 22 ms / Memory 13.3 MB    
    def rotateRight_2(self, head, k):
        # empty data
        if not head or not head.next:
            return head

        # calculate step
        cnt = 1
        a = head
        while a.next:
            cnt += 1
            a = a.next
        step = k % cnt
        
        # return
        if step == 0:
            return head
        # [a(n),b(l-n)],a(n),b(l-n) = a(n),[b(l-n),a(n)],b(l-n)
        a.next = head #[head[-1]->head->head->...]
        for i in range(cnt-step):
            a = a.next
        
        b = a.next #connect b
        a.next = None #cut end

        return b

        #  [5], 1 , 2 , 3 , 4 ,[5], 1 , 2 , 3 , 4 ,... => a.next = head
        #a: 5 , 1 , 2 ,[a], 4 , 5 , 1 , 2 ,[a], 4 ,... => Loop: a.next
        #b: 5 , 1 , 2 ,[a],[b], 5 , 1 , 2 ,[a],[b],... => b = a.next
        #a:                [b], 5 , 1 , 2 ,[a]         => a.next = None