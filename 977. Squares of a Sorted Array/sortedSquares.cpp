class Solution {
public:
    vector<int> sortedSquares(vector<int>& nums) {
        int n = nums.size();
        vector<int> result(n);

        int L = 0;
        int R = n-1;

        for (int i = n-1; i>=0; i--) {
            int square;
            if (abs(nums[L]) > abs(nums[R])) {
                square = abs(nums[L]); L++;
            }
            else {
                square = abs(nums[R]); R--;
            }
            result[i] = square * square;

        }
        return result;
    }
};