# -*- coding: utf-8 -*-
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    # Runtime 37 ms / Memory 13.5 MB
    def deleteNode_1(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        a = node
        while a.next:
            a.val = a.next.val #val change next
            b = a
            a = a.next #step to next
        b.next = None #clear last
    
    # Runtime 26 ms / Memory 13.8 MB
    def deleteNode_2(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val #val change next
        node.next = node.next.next #node change next



if __name__ == '__main__':
    print("=====================================")