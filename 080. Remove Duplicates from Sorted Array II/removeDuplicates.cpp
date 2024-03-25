class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        if (nums.size()<=2) { return nums.size(); } //Q: at most twice
        // else
        int i = 2; //slow
        int j = 2; //fast

        for (j=2; j<nums.size(); ++j) {
            if (nums[j] != nums[i-2]) {
                nums[i] = nums[j];
                ++i;
            }
        }
        return i;
    }
};