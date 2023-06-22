# -*- coding: utf-8 -*-

# Runtime 452 ms / Memory 16.4 MB
class MyHashMap_1(object):

    def __init__(self):
        self.HashMap = {}
        

    def put(self, key, value):
        self.HashMap[key] = value
        

    def get(self, key):
        if key in self.HashMap.keys():
            return self.HashMap[key]
        return -1
        

    def remove(self, key):
        if key in self.HashMap.keys():
            self.HashMap.pop(key)


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)



# Runtime 250 ms / Memory 17.6 MB
class ListNode:
    def __init__(self, key, val, nxt):
        self.key = key
        self.val = val
        self.next = nxt

class MyHashMap_2:
    def __init__(self):
        self.size = 10000
        self.mult = 1000001
        self.data = [None for _ in range(self.size)]

    def hash(self, key):
        return key * self.mult % self.size
    
    def put(self, key, val):
        self.remove(key)
        h = self.hash(key)
        node = ListNode(key, val, self.data[h])
        self.data[h] = node

    def get(self, key):
        h = self.hash(key)
        node = self.data[h]
        while node:
            if node.key == key: return node.val
            node = node.next
        return -1
    
    def remove(self, key):
        h = self.hash(key)
        node = self.data[h]
        if not node:
            return
        if node.key == key:
            self.data[h] = node.next
            return
        while node.next:
            if node.next.key == key:
                node.next = node.next.next
                return
            node = node.next