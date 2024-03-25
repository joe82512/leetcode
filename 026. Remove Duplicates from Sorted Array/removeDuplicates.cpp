class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        // two-pointer
        int i=1; //slow
        int j=1; //fast

        for (j=1; j<nums.size(); ++j) {
            if (nums[j] !=nums[i-1]) { //i-1 or j-1
                nums[i] = nums[j];
                ++i;
            }
        }
        return i;
    }
};