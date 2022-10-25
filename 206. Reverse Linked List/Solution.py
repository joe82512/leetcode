# -*- coding: utf-8 -*-
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    # Runtime 25 ms / Memory 15.4 MB
    def reverseList_1(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        r = None
        while head:
            temp = head.next
            head.next = r
            r = head
            head = temp
            # head.next, r, head = r, head, head.next
        return r
    
    # Runtime 15 ms / Memory 18.9 MB
    def reverseList_2(self, head):
        return self.reverse(head,None)
        
    def reverse(self,head,r):
        if not head:
            return r
        temp = head.next
        head.next = r
        return self.reverse(temp, head)



if __name__ == '__main__':
    print("=====================================")