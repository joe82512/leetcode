class Solution {
public:
    int arraySign(vector<int>& nums) {
        int r = 1;
        for (auto num:nums) {
            if (num==0) { return 0; } //0*n=0
            else if (num<0) { r = r * (-1); } //neg *-1, pos *1
        }
        return r;
    }
};