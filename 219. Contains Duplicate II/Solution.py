class Solution(object):
    # Runtime 463 ms / Memory 22.8 MB
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        #只要有距離小於k就True
        t = {} #{num: last_idx}
        for (idx,num) in enumerate(nums):
            if (num in t) and (idx-t[num]<=k):
                return True
            else:
                t[num] = idx
        return False
        