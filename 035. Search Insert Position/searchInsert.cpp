class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        int L = 0;
        int R = nums.size()-1;
        int mid = L + (R-L)/2;

        // Boudary
        if (target>nums[R]) { return R+1; }
        else if (target<nums[L]) { return 0; }
        else if (L==R) {return 0; }  //for 1 element

        while (L<=R) {
            // match
            if (nums[mid]==target) { return mid; }
            // no match : LR step
            else if(nums[mid]<target){ L = mid+1; }
            else { R = mid-1; }
            // update mid
            mid = L + (R-L)/2;
        }
        return L;
    }
};