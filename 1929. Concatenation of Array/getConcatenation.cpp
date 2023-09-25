class Solution {
public:
    vector<int> getConcatenation(vector<int>& nums) {
        vector<int> temp = nums; //copy
        nums.insert(nums.end(), temp.begin(), temp.end()); //add
        return nums;
    }
};