# -*- coding: utf-8 -*-
class Solution(object):
    # Runtime 1382 ms / Memory 22.7 MB
    def maxProfit_1(self, prices):
        profit = 0
        buy = prices[0]
        for p in prices:
            buy = min(p,buy)
            profit = max(profit, p-buy)
        return profit

    # Runtime 1163 ms / Memory 22.7 MB
    def maxProfit_2(self, prices):
        profit = 0
        buy = prices[0]
        for p in prices:
            new_profit = p - buy
            if new_profit < 0: # min(b,buy)
                buy = p
            elif new_profit > profit: # max(profit, p-buy)
                profit = new_profit
        return profit



if __name__ == '__main__':
    print(Solution().maxProfit_1([7,1,5,3,6,4]))
    print(Solution().maxProfit_1([7,6,4,3,1]))
    print("=====================================")
    print(Solution().maxProfit_2([7,1,5,3,6,4]))
    print(Solution().maxProfit_2([7,6,4,3,1]))