# -*- coding: utf-8 -*-
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    # Runtime 79 ms / Memory 22.3 MB
    def mergeKLists_1(self, lists):
        arr = []
        for l in lists:
            node = l
            while node:
                arr.append(node.val)
                node = node.next
        arr.sort()
        # 正向建立linked-list
        root = temp = ListNode(None)
        for i in arr:
            temp.next = ListNode(i)
            temp = temp.next
        """
        #反向建立linked-list
        arr.reverse()
        root = None
        for i in arr:
            root = ListNode(i,root)
        return root
        """
        return root.next

    # Runtime 85 ms / Memory 19.5 MB
    def mergeKLists_2(self, lists):
        if not lists:
            return None
        if len(lists) == 1:
            return lists[0]
        
        mid = len(lists) // 2
        left = self.mergeKLists_2(lists[:mid])
        right = self.mergeKLists_2(lists[mid:])
        
        return self.merge(left, right)
    
    def merge(self, l1, l2):
        dummy = ListNode(0)
        curr = dummy
        
        while l1 and l2:
            if l1.val < l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next
        
        curr.next = l1 or l2
        
        return dummy.next