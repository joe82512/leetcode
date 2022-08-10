# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    # Runtime 32 ms / Memory 13.2 MB
    def removeNthFromEnd_1(self, head, n):
        r = head
        count = 0
        while(r):
            count += 1
            r = r.next
        
        r = result = ListNode()        
        p = count - n
        
        r.next = head
        for i in range(p):
            r = r.next
        r.next = r.next.next
        
        return result.next

    # Runtime 35 ms / Memory 13.5 MB
    def hasCycle_2(self, head, n):
        fast = slow = head
        for i in range(n):
            fast = fast.next
        
        if not fast:
            return head.next
        while fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return head



if __name__ == '__main__':
    print("=====================================")   