class Solution {
public:
    vector<int> runningSum(vector<int>& nums) {
        // start from inedx 1
        for (int i=1; i<nums.size(); i++) {
            nums[i] += nums[i-1]; //accumulate
        }
        return nums;
    }
};