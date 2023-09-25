class Solution {
public:
    int numTrees(int n) {
        /*
        f(0) = 1;
        f(1) = 1;
        f(2) = f(1)*f(0) -> only left tree
              +f(0)*f(1) -> only right tree
             = 2;
        f(3) = f(2)*f(0) -> only left tree
              +f(1)*f(1) -> 1 L 1 R
              +f(0)*f(2) -> only right tree
             = 5;
            ...
        f(n) = f(0) * f(n-1) + f(1) * f(n-2) + … + f(n-1) * f(0);
        */
        vector<int> dp(n+1);
        dp[0] = dp[1] = 1;
        for (int i=2; i<n+1; i++) {
            for (int j=0; j<i; j++) {
                dp[i] += dp[j] * dp[i-j-1];
            }
        }
        return dp[n];
    }
};