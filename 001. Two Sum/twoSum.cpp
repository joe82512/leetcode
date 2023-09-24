class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> hashMap; //{value:index}
        int n = nums.size();     

        for (int i=0; i<n; i++) {
            int diff, val;
            val = nums[i];
            diff = target - val;
            if (hashMap.find(val)!=hashMap.end()) { //key exist
                return {hashMap[val], i}; //{diff_index,value_index}
            }
            else {
                hashMap[diff] = i; //{diff:val_index}
            }
        }

        return {};
    }
};