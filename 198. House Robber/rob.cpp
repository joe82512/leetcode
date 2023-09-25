class Solution {
public:
    int rob(vector<int>& nums) {
        // dp: F(n) = max(F(n-2)+nums[n], F(n-1)+0)
        int n = nums.size();
        // runtime ERROR //
        // int a = nums[0]; //F0
        // if (n == 0) { return a; }
        
        // int b = max(nums[0],nums[1]); //F1
        // if (n == 1) { return b; }

        // for (int i=2; i<n; i++) {
        //     int temp = b;
        //     b = max(a+nums[i],b);
        //     a = temp;
        // }
        // return b;
        vector<int> dp(n+1,0);
        for(int i=1; i<n+1; i++){
            if (i==1) { dp[i] = max(nums[i-1],dp[i-1]); }
            else { dp[i] = max(nums[i-1]+dp[i-2] ,dp[i-1]); }
        }  
        return dp[n];
    }
};