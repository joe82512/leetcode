class Solution {
public:
    vector<int> answerQueries(vector<int>& nums, vector<int>& queries) {
        sort(nums.begin(),nums.end());
        // create accumulator
        vector<int> add_nums;
        int temp = 0;
        for (auto num:nums) {
            temp = temp + num;
            add_nums.push_back(temp);
        }
        // get index as number of element
        vector<int> output;
        for (auto tar:queries) {
            int idx = upper_bound(add_nums.begin(),add_nums.end(),tar) - add_nums.begin(); //binary search func
            output.push_back(idx);
        }
        return output;
    }
};