class Solution(object):
    # Runtime 36 ms / Memory 11.5 MB
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if (len(nums)<=2): #Q: at most twice
            return len(nums)
        #else, two pointer
        i = 2 #slow
        for j in range(2,len(nums)): #fast
            if (nums[j] != nums[i-2]): #not j-2 !
                nums[i] = nums[j]
                i = i+1
        return i