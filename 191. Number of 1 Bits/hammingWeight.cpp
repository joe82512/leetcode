class Solution {
public:
    int hammingWeight(uint32_t n) {
        int r = 0;
        while (n) {
           r = r + (n&1); //get Least bit
           n = n >> 1; //shift Least bit
        }
        return r;
    }
};