class Solution {
public:
    int maxProfit(vector<int>& prices) {
        // EX: 1->2->3->4->5 買賣5次結果也是賺價差1*4=4
        int res = 0;
        for (int i=1; i<prices.size(); ++i) {
            int temp = prices[i] - prices[i-1];
            if (temp >0 ) { res += temp; }
        }
        return res;
    }
};