# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    # Runtime 374 ms / Memory 69.4 MB
    def sortList_1(self, head): #sort with array
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # array sort: time O(logn)
        # create array : space O(n)

        if not head:
            return None
        
        # create array
        node = head
        arr = []
        while (node):
            arr.append(node.val)
            node = node.next
        
        # sort
        arr.sort()

        # recover linked-list
        dummy = ListNode(0)
        node = dummy
        for a in arr:
            node.next = ListNode(a)
            node = node.next
            
        return dummy.next
    
    # Runtime 750 ms / Memory 52.7 MB
    def sortList_2(self, head): #merge sort
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # merge sort: time O(nlogn)
        # without recursion: space O(logn) -> O(1)
        # ref: https://leetcode.com/problems/sort-list/solutions/3417365/c-java-python-javascript-memory-o-1-3-approaches-linked-list/
        
        if not head or not head.next:
            return head

        length = self.getLength(head)
        dummy = ListNode(0)
        dummy.next = head

        step = 1
        while step < length: #O(logn) by step
            curr = dummy.next
            tail = dummy #initial

            # O(n) = O(n/step) * O(step)
            while curr: #O(n/step)
                left = curr
                # O(step)
                right = self.split(left, step) #len(right)=1,2,...
                curr = self.split(right, step) #len(curr) =1,2,... ; curr = left.(next*step)
                # O(step)
                tail = self.merge(left, right, tail) #sort & merge & go end

            step = step*2 #1,2,4,8,...

        return dummy.next #ignore dummy

    # get linked-list total length
    def getLength(self, head):
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next
        return length

    # split
    def split(self, head, step):
        if head is None:
            return None

        for i in range(1, step):
            if head.next is None:
                break
            head = head.next

        right = head.next
        head.next = None
        return right

    # merge with sort
    def merge(self, left, right, tail):
        curr = tail
        while left and right:
            # sort
            if left.val < right.val:
                curr.next = left
                left = left.next
            else:
                curr.next = right
                right = right.next
            curr = curr.next

        curr.next = left if left else right
        while curr.next:
            curr = curr.next

        return curr
    


    """
    case 1: [4,2,1,3]
    step(1). 0->[2]->4 | 4->[1]->3
    step(2). 0->[1]->2->3->4

    case 2: [-1,5,3,4,0]
    step(1). 0->[-1]->5 | 5->[3]->4 | 4->[0]
    step(2). 0->[-1]->3->4->5 | 5->[0]
    step(4). 0->[-1]->0->3->4->5

    case: [8,7,6,5,4,3,2,1]
    step(1). 0->[7]->8 | 8->[5]->6 | 6->[3]->4 | 4->[1]->2
    step(2). 0->[5]->6->7->8 | 8->[1]->2->3->4
    step(4). 0->[1]->2->3->4->5->6->7->8
    """