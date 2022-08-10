# -*- coding: utf-8 -*-
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    # Runtime 1812 ms / Memory 85.3 MB
    def isPalindrome_1(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        a = head
        a_list = []
        while a:
            a_list.append(a.val)
            a = a.next
        return a_list == a_list[::-1]

    # Runtime ms / Memory B
    def isPalindrome_2(self, head):
        pass



if __name__ == '__main__':
    print("=====================================")   