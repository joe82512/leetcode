class Solution {
public:
    void rotate(vector<int>& nums, int k) {
        int n = nums.size();
        k = k % n; //sequence loop
        // recombine
        vector<int> output(n);
        for (int i=0; i<n; i++) {
            if (i+k>=n) { output[(i+k)-n] = nums[i]; }
            else { output[(i+k)] = nums[i]; }
        }
        nums = output;
    }
};