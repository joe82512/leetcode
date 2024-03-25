class Solution {
public:
    int coinChange(vector<int>& coins, int amount) {
        // dp[idx]=min(cnt), idx=sum of coin
        vector<int> dp(amount+1, 1e4+1);
        dp[0] = 0;

        sort(coins.begin(), coins.end());
        for (int i=1; i<amount+1; ++i) { //sum of coin
            for (auto coin:coins) {
                if (coin <= i) {
                    dp[i] = min(dp[i], dp[i - coin] + 1); //get min count
                }
                else { break; } //early break
            }
        }

        if (dp[amount]==1e4+1) { return -1; } //#no combine
        else { return dp[amount]; }
    }
};