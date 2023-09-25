class Solution {
public:
    int findMin(vector<int>& nums) {
        // binary search tree O(log(n))
        // find small
        int L = 0, R = nums.size()-1;
        while (L < R) {
            int mid = L + (R-L)/2;
            if (nums[mid] < nums[R]) { R = mid; }
            else { L = mid + 1; }
        }
        return nums[L];
    }
};