class Solution {
public:
    int singleNumber(vector<int>& nums) {
        int res = 0;
        for (int i=0; i<32; i++) {
            int sum_bit = 0;
            for (auto num:nums) {
                int bit = (num >> i) & 1; //get bit on idx i
                sum_bit = sum_bit + bit; //sum bit on idx i
            }
            sum_bit = sum_bit % 3; //1or0
            res = res | (sum_bit << i); //recover idx and set res
        }

        return res;
    }
};