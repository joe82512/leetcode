import random
# Runtime 308 ms / Memory 57.7 MB
class RandomizedSet(object):

    def __init__(self):
        self.hashmap = {} #{val: idx}
        self.vals = []


    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val in self.hashmap:
            return False
        #else:
        self.hashmap[val] = len(self.vals) #last
        self.vals.append(val)
        return True
        

    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val not in self.hashmap:
            return False
        #else:
        # search:O(1) if hashmap , but dict O(logn)
        idx = self.hashmap[val]
        # copy and cover last as target
        last_val = self.vals[-1]
        self.hashmap[last_val] = idx
        self.vals[idx] = last_val
        # delete last
        del self.hashmap[val]
        self.vals.pop()
        return True
        """
        ex: remove 5 from [4,5,6,7]
        [4,5,6,7] -> [4,7,6,7] -> [4,7,6] _ unstable
        """

    def getRandom(self):
        """
        :rtype: int
        """
        return random.choice(self.vals) #constant


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()