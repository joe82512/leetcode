class Solution {
public:
    int majorityElement(vector<int>& nums) {
        // get middle number
        sort(nums.begin(),nums.end());
        int n = nums.size();
        return nums[n/2];
    }
};