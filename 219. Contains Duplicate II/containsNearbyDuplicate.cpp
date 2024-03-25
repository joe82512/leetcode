class Solution {
public:
    bool containsNearbyDuplicate(vector<int>& nums, int k) {
        // if distance less than k, return true
        unordered_map<int,int> t; //{num: last_idx}
        for (int idx=0; idx<nums.size(); ++idx) {
            if (t.find(nums[idx])!=t.end() && idx-t[nums[idx]]<=k) {
                return true;
            }
            else {
                t[nums[idx]] = idx;
            }
        }
        return false;
    }
};