class Solution(object):
    # Runtime 49 ms / Memory 13.4 MB
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # two-pointer
        i = 1 #slow
        for j in range(1, len(nums)): #fast
            if (nums[j] !=nums[i-1]): #i-1 or j-1
                nums[i] = nums[j]
                i = i+1
        return i