class Solution(object):
    # Runtime 37 ms / Memory 14.6 MB
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        res = 0
        for i in range(1,len(prices)):
            temp = prices[i]-prices[i-1] #價差
            if (temp>0):
                res += temp #賺就買賣
        return res
        #Example2 1->2->3->4->5 買賣5次結果也是賺價差1*4=4