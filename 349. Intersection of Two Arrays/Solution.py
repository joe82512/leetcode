# -*- coding: utf-8 -*-
class Solution:
    # Runtime 52 ms / Memory 13.6 MB
    def intersection_1(self, nums1, nums2):
        return list(set(nums1)&set(nums2))

    # Runtime  / Memory 
    def intersection_2(self, nums1, nums2):
        pass



if __name__ == '__main__':
    print(Solution().intersection_1([1,2,2,1],[2,2]))
    print(Solution().intersection_1([4,9,5],[9,4,9,8,4]))
    print("=====================================")