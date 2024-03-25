class Solution(object):
    # Runtime 47 ms / Memory 11.7 MB
    def rangeBitwiseAnd_1(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        # 計算最高值, 因為有遇到進位一定會造成全0
        shift = 0 #位移次數 
        while left < right: #L==R break
            left =  (left>>1)
            right = (right>>1)
            shift += 1
        return left << shift
        """
        L : 1101010 -> 110101 -> 11010 -> 1101 => 1101000
        R : 1101111 -> 110111 -> 11011 -> 1101
        """

    # Runtime 53 ms / Memory 11.6 MB
    def rangeBitwiseAnd_2(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        while (right > left):
            right = right & (right - 1) #反著做
        return right