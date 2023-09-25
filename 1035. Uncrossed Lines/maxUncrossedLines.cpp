class Solution {
public:
    int maxUncrossedLines(vector<int>& nums1, vector<int>& nums2) {
        // keep nums1 > nums2
        if (nums1.size() < nums2.size()) { swap(nums1,nums2); }
        // DP 2 loop
        int m = nums1.size(), n = nums2.size();
        vector<int> dp(n+1,0); //{0*n+1} 1-D vector
        for (int i=1; i<m+1; i++) {
            int prev = 0;
            for (int j=1; j<n+1; j++) {
                int curr = dp[j];
                // find same sequence
                if (nums1[i-1]==nums2[j-1]) { dp[j] = prev + 1; }
                else { dp[j] = max(dp[j-1], curr); }
                prev = curr; //update
            }
        }
        return dp[n]; //last element
    }
};