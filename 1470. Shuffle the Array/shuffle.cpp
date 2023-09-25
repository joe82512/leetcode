class Solution {
public:
    vector<int> shuffle(vector<int>& nums, int n) {
        vector<int> r;
        for (int i=0; i<n; i++) {
            r.push_back(nums[i]); //x
            r.push_back(nums[i+n]); //y
        }
        return r;
    }
};