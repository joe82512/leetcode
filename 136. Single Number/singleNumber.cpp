class Solution {
public:
    int singleNumber(vector<int>& nums) {
        int r = nums[0];
        for (int i=1; i<nums.size(); i++) {
            r = r ^ nums[i]; //XOR:00->0 11->0 01->1
        }
        return r;
    }
};