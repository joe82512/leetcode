class Node:
    def __init__(self, key, val, prev=None, next=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next

# Runtime 776 ms / Memory 78.4 MB
class LRUCache(object):
    # hashmap -> search: O(1)
    # linked-list -> insert: O(1)
    # double linked-list -> insert: O(1) / remove: O(1)
    # combine hashmap + double linked-list
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cap = capacity
        # double linked-list: cap+2, cause dummy head and dummy tail
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        (self.head.next,self.tail.prev) = (self.tail,self.head)
        # hashmap , dict not hashmap in fact
        self.hashmap = {} #{key, pointer} 
    
    # double linked-list insert
    def insertHead(self, node):
        node.next, node.prev = self.head.next, self.head
        self.head.next.prev = node
        self.head.next = node
        """
        head <----------> N
        head <-> node <-> N
        """

    # double linked-list remove
    def remove(self, node):
        (node.prev.next, node.next.prev) = (node.next, node.prev)
        """
        N0 <-> node <-> N1
        N0 <----------> N1
        """

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        # if exist, move to front
        if key in self.hashmap:
            node = self.hashmap[key]
            value = node.val
            #delete
            del self.hashmap[key]
            self.remove(node)
            #combine, move to front
            self.insertHead(node)
            self.hashmap[key] = self.head.next #not head
            return value
        #else:
        return -1
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        # step1. delete if update
        if key in self.hashmap:
            node = self.hashmap[key]
            del self.hashmap[key]
            self.remove(node)

        # step1. delete tail.prev if overflow
        if len(self.hashmap) == self.cap:
            del self.hashmap[self.tail.prev.key] #not tail
            self.remove(self.tail.prev)

        # step2. combine, move to front
        self.insertHead(Node(key, value))
        self.hashmap[key] = self.head.next


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)