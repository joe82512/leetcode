# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    # Runtime 72 ms / Memory 20.7 MB
    def hasCycle_1(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        a = head
        b = head
        while b and b.next: #empty link
            a = a.next
            b = b.next.next
            if a == b: #val & next must equal
                return True
        return False

    # Runtime ms / Memory B
    def hasCycle_2(self, head):
        pass



if __name__ == '__main__':
    print("=====================================")   