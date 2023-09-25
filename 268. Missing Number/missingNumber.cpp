class Solution {
public:
    int missingNumber(vector<int>& nums) {
        // pair XOR = 0
        int r = 0;
        for(int num:nums){ r = r^num; }
        for(int i=0; i<=nums.size(); i++){ r = r^i; }
        return r;
    }
};