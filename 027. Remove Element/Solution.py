# -*- coding: utf-8 -*-
class Solution:
    # Runtime 31 ms / Memory 13.4 MB
    def removeElement_1(self, nums, val):
        n = nums.count(val)
        k = len(nums) - n
        for i in range(n):
            nums.remove(val)
        return k

    # Runtime 11 ms / Memory 13.4 MB
    def removeElement_2(self, nums, val):
        for i in reversed(range(len(nums))):
            # 須反向, 否則index會受pop影響
            if nums[i] == val:
                nums.pop(i)
        return len(nums)



if __name__ == '__main__':
    print(Solution().removeElement_1([3,2,2,3],3))
    print(Solution().removeElement_1([0,1,2,2,3,0,4,2],2))
    print("=====================================")
    print(Solution().removeElement_2([3,2,2,3],3))
    print(Solution().removeElement_2([0,1,2,2,3,0,4,2],2))