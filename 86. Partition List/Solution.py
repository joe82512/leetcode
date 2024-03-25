# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution(object):
    # Runtime 15 ms / Memory 11.8 MB
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        # two poniter
        leftList = goLeft = ListNode(0) #dummy head
        rightList = goRight = ListNode(0) #dummy head

        while (head):
            if (head.val < x):
                goLeft.next = head
                goLeft = goLeft.next
                # print("A:",goLeft.val)
            else:
                goRight.next = head
                goRight = goRight.next
                # print("B:",goRight.val)
            head = head.next

        goLeft.next = rightList.next #combine, ignore dummy (rightList) head
        goRight.next = None #tail
        return leftList.next #ignore dummy head