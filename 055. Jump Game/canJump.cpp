class Solution {
public:
    bool canJump(vector<int>& nums) {
        int n = nums.size();
        int position = 0;
        for (int i=0; i<n; i++) {
            if (i>position) { return false; } //cant goal next place
            // else
            position = max(position, i+nums[i]); //go max step
            if (position >= n-1) { return true; }
        }

        return true; //just for structure
    }
};