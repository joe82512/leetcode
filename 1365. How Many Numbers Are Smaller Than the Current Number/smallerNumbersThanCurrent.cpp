class Solution {
public:
    vector<int> smallerNumbersThanCurrent(vector<int>& nums) {
        vector<int> idx_nums;
        vector<int> sort_nums = nums;
        sort(sort_nums.begin(),sort_nums.end());

        for (auto num:nums) {
            // find num in sort_nums
            vector<int>::iterator iter=find(sort_nums.begin(),sort_nums.end(),num);
            // return index in sort_nums
            idx_nums.push_back(distance(sort_nums.begin(),iter));
        }
        
        return idx_nums;
    }
};