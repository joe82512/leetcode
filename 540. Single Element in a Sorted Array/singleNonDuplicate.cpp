class Solution {
public:
    int singleNonDuplicate(vector<int>& nums) {
        // O(logn) -> binary search
        int L=0, R=nums.size()-1;
        int mid;
        while (L < R) {
            mid = L + (R-L)/2;
            // get even
            if (mid%2 == 1) { mid--; }
            // LR
            if (nums[mid] != nums[mid+1]) { R = mid; } //result in left
            else { L = mid+2; } //pair
        }
        return nums[L];
    }
};