class Solution(object):
    # Runtime 97 ms / Memory 12.8 MB
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cnt = 0 #counter
        idxMaxPosition = 0 #每個位置最長能到位置
        resMaxPosition = 0 #目前能到的最大距離

        # special case
        if len(nums)<=1: #[0]
            return 0

        # 題目預設必能達到終點
        for i in range(len(nums)):
            idxMaxPosition = max(idxMaxPosition, i + nums[i]) #update

            if (i==resMaxPosition): #到達最大距離
                resMaxPosition = idxMaxPosition #update
                cnt += 1
                if (idxMaxPosition >= len(nums)-1): #足夠到最末位置
                    break

        return cnt