class Solution {
public:
    vector<vector<int>> res;
    void dfs (int idx, vector<int> nums) {
        if (idx >= nums.size()) {
            res.push_back(nums);
            return;
        }
        else {
            /*
            for (auto n:nums) {
                cout << n;
            }
            cout << endl;
            */
            for (int i=idx; i<nums.size(); i++) {
                if (i != idx && nums[i]==nums[idx]) {
                    continue;
                }                
                swap(nums[i], nums[idx]);
                dfs(idx+1,nums);
            }
        }
    }
    vector<vector<int>> permuteUnique(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        dfs(0, nums);
        return res;
    }
};