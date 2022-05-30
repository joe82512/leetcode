# -*- coding: utf-8 -*-
class Solution:
    # Runtime 55 ms / Memory 13.6 MB
    def intersect_1(self, nums1, nums2):
        nums1.sort()
        nums2.sort()
        r = {}
        if len(nums1) < len(nums2):
            for i,v in enumerate(nums1):
                if v in nums2:
                    nums2.remove(v)
                    r[i] = v
        else:
            for i,v in enumerate(nums2):
                if v in nums1:
                    nums1.remove(v)
                    r[i] = v
        return r.values()

    # Runtime  / Memory 
    def intersect_2(self, nums):
        pass



if __name__ == '__main__':
    print(Solution().intersect_1([1,2,2,1],[2,2]))
    print(Solution().intersect_1([4,9,5],[9,4,9,8,4]))
    print("=====================================")