# -*- coding: utf-8 -*-
class Solution:
    # Runtime 127 ms / Memory 13.6 MB
    def findMedianSortedArrays_1(self, nums1, nums2):
        nums = sorted(nums1+nums2)
        if len(nums)%2 == 0:
            n = [len(nums)/2-1,len(nums)/2]
        else:
            n = [(len(nums)-1)/2,(len(nums)-1)/2] 
        result = nums[n[0]]+nums[n[1]]
        return float(result)/2

    # Runtime 136 ms / Memory 13.4 MB
    def findMedianSortedArrays_2(self, nums1, nums2): #Note
        # WE SHALL DO BINARY SEARCH ON THE SMALLER ARRAY, NUMS1
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)
        
        # SETUP INT_MIN AND INT_MAX FOR EMPTY LEFT / RIGHT PARTITION
        INT_MIN, INT_MAX = -2**64, 2**64
        
        # SETUP LO AND HI POINTERS
        lo, hi = 0, len(nums1)
        left_partition_size = (len(nums1) + len(nums2) + 1) // 2
        n = len(nums1) + len(nums2)
        
        # LOOP TILL OOB
        while lo <= hi:
            
            # GET THE PARITIONS OF BOTH ARRAYS
            p1 = (lo + hi) // 2
            p2 = left_partition_size - p1

            # GET THE 4 BOUNDARY NUMBERS
            nums1_left = nums1[p1 - 1] if p1 > 0 else INT_MIN
            nums1_right = nums1[p1] if p1 < len(nums1) else INT_MAX
            
            nums2_left = nums2[p2 - 1] if p2 > 0 else INT_MIN
            nums2_right = nums2[p2] if p2 < len(nums2) else INT_MAX
            
            # MOVE P1 LEFTWARDS
            if nums1_left > nums2_right:
                hi = p1 - 1
            
            # MOVE P1 RIGHTWARDS
            elif nums2_left > nums1_right:
                lo = p1 + 1
            
            # CORRECT PARTITION FOUND
            else:
                
                # ODD TOTAL LENGTH
                if n & 1:
                    return max(nums1_left, nums2_left)
                
                # EVEN TOTAL LENGTH
                return (max(nums1_left, nums2_left) + min(nums1_right, nums2_right)) / 2.0



if __name__ == '__main__':
    print(Solution().findMedianSortedArrays_1([1,3],[2]))
    print(Solution().findMedianSortedArrays_1([1,2],[3,4]))
    print("=====================================")
    print(Solution().findMedianSortedArrays_2([1,3],[2]))
    print(Solution().findMedianSortedArrays_2([1,2],[3,4]))



#Binary search
#Let's go through an example of the question
#Time: O(log(min(m,n))
#Space: O(1)
#   A      : [2 4 6]
#   B      : [1 3 5]
#   Final  : [1 2 3 4 5 6]
#   Median : (3 + 4) / 2 = 3.5
#Next, we want to generate all possible partitions of A and B. Since both are sorted, we guarantee that these are the only possible partitions

#A      : [ | 2 4 6]    L : [1 3 5]
#B      : [1 3 5 | ]    R : [2 4 6] ----- ❌, since 5 > 2

#A      : [2 | 4 6]     L : [1 2 3]
#B      : [1 3 | 5]     R : [4 5 6] ----- ✔, since 2 < 5 and 3 < 4

#A      : [2 4 | 6]     L : [1 2 4]
#B      : [1 | 3 5]     R : [3 5 6] ----- ❌, since 4 > 3

#A      : [2 4 6 | ]    L : [2 4 6]
#B      : [ | 1 3 5]    R : [1 3 5] ----- ❌, since 6 > 1
#Q : How do we know if a partition is valid (ie. all values in L <= all values in R?

#	We  only need to compare the 4 elements adjacent to the 2 partitions
#Q : How do we represent empty partitions?

#If it's a empty left partition, we use INT_MIN
#else, we use INT_MAX
#	We only need to check the 4 elements adjacent to the partition borders

#With that, we build our solution