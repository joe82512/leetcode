class Solution {
public:
    vector<int> searchRange(vector<int>& nums, int target) {
        vector<int> res = {-1,-1};
        
        // binary search for first
        int L = 0; 
        int R = nums.size();
        while (L < R) {
            int mid = L + (R-L)/2;
            if (nums[mid] < target) { L = mid+1; }
            else { R = mid; }
        }
        // no match
        if (R==nums.size() || nums[R]!=target) { return res; }
        // get fisrt 
        res[0] = R;
        
        // binary search for last
        R = nums.size();
        while (L < R) {
            int mid = L + (R-L)/2;
            if (nums[mid] <= target) { L = mid+1; } //same value go next
            else { R = mid; }
        }
        // get last
        res[1] = R - 1;
        return res;
    }
};