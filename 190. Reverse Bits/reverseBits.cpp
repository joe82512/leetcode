class Solution {
public:
    uint32_t reverseBits(uint32_t n) {
        uint32_t out = 0;
        for (int i=0; i<32; i++) {
            out = out << 1;
            if (n&1==1) { //n%2==1
                out += 1;
            }
            n = n >> 1;
        }
        return out;
    }
};