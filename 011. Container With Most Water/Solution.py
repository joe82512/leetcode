class Solution(object):
    # Runtime 1369 ms / Memory 23.7 MB
    def maxArea_1(self, height):
        left = 0
        right = len(height)-1
        res = 0

        while right > left:
            area = (right-left) * min(height[right],height[left])
            res = max(area,res)

            if height[left] > height[right]:
                right -= 1
            else:
                left += 1

        return res

    # Runtime ms / Memory MB
    def maxArea_2(self, height):
        pass