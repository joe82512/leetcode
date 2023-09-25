class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int profit = 0;
        int buy = prices[0];
        // DP
        for (auto price:prices) {
            if (buy > price) { buy = price; } //low cost
            profit = max(profit, price-buy); //best profit
        }

        return profit;
    }
};