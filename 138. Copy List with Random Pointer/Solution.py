# -*- coding: utf-8 -*-
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random

from collections import defaultdict
class Solution(object):
    # Runtime 80 ms / Memory 14.4 MB
    def copyRandomList_1(self, head):
        # Base case
        if not head: return None
        
        # Init
        curr = Node(head.val)
        result = Node(0, next=curr)
        mp = {head: result.next}
        
        # Traversal
        while head:
            # Next part
            if not head.next:
                curr.next = None
            elif head.next in mp: #random already add
                curr.next = mp[head.next]
            else:
                curr.next = Node(head.next.val)
                mp[head.next] = curr.next
            
            # Random part
            if not head.random:
                curr.random = None
            elif head.random in mp:
                curr.random = mp[head.random]
            else:
                curr.random = Node(head.random.val)
                mp[head.random] = curr.random
            
            # Step
            head = head.next
            curr = curr.next
                
        return result.next

    # Runtime 54 ms / Memory 14.1 MB
    def copyRandomList_2(self, head):
        def defaultValueFormat():
            return Node(0)
        dic = defaultdict(defaultValueFormat) # no()
        #dic = defaultdict(lambda: Node(0))
        dic[None] = None #set null
        n = head
        while n:
            dic[n].val = n.val
            dic[n].next = dic[n.next]
            dic[n].random = dic[n.random]
            n = n.next
        return dic[head]