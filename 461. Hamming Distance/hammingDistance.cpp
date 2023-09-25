class Solution {
public:
    int hammingDistance(int x, int y) {
        int cnt = 0;
        int p = x^y; //XOR
        while (p) {
            cnt += (p&1); //get least bit
            p = p >> 1; //shift for update least bit
        }
        return cnt;
    }
};