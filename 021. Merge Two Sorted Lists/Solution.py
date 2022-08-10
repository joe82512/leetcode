# -*- coding: utf-8 -*-
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    # Runtime 35 ms / Memory 13.6 MB
    def mergeTwoLists_1(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        r = result = ListNode()
        while list1 and list2:
            if list1.val <= list2.val:
                r.next = list1 #change connect link
                list1 = list1.next #step to next
                
            else:
                r.next = list2
                list2 = list2.next
            r = r.next #step to next
        
        if list1 or list2:
            r.next = list1 if list1 else list2 #connect link
        
        return result.next #link step reset

    # Runtime 49 ms / Memory 13.6 MB
    def mergeTwoLists_2(self, list1, list2):
        if not list1 or not list2:
            return list1 or list2
        if list1.val > list2.val: #swap min
            list1, list2 = list2, list1
        list1.next = self.mergeTwoLists_2(list2,list1.next) #connect link

        return list1



if __name__ == '__main__':
    print("=====================================")   