class Solution {
public:
    int minSubArrayLen(int target, vector<int>& nums) {
        int max_num = *max_element(nums.begin(), nums.end());
        if (max_num>=target) { return 1; }
        //else{ }
        int res = nums.size()+1; //more than impossible
        int temp_sum = 0;
        int L = 0, R = 0;
        for (R=0; R<nums.size(); ++R) {
            temp_sum = temp_sum + nums[R]; //slide window
            while (temp_sum >= target) {   //early break
                res = min(res, R-L+1);
                temp_sum = temp_sum - nums[L];
                ++L;
            }
        }

        return (res>nums.size()) ? 0 : res ;
    }
};