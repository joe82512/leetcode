class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        sort(nums.begin(),nums.end());
        vector<vector<int>> output;
        for (int i=0; i<nums.size(); i++) {
            // early stop
            if (nums[i]>0) { break; }
            // same value
            if (i>0 and nums[i-1]==nums[i]) { continue; }
            // two pointer
            int j = i+1; //L
            int k = nums.size()-1; //R
            while (j<k) {
                int total = nums[i]+nums[j]+nums[k];
                if (total == 0) {
                    output.push_back({nums[i],nums[j],nums[k]});
                    j++; k--; //all step
                    while(j<k & nums[j-1] == nums[j]) { j++; } //same L
                    while(j<k & nums[k+1] == nums[k]) { k--; } //same R
                }
                else if (total<0) { j++; } //L step
                else if (total>0) { k--; } //R step
            }
        }
        return output;
    }
};