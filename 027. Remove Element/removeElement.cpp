class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int j = 0;
        for (int i=0; i<nums.size();) {
            //pop(i), but index change
            if (nums[i]==val) {
                nums.erase(nums.begin()+i);
                j++; //avoid index change
            }
            else {
                i++;
            }
        }
        return nums.size();
    }
};