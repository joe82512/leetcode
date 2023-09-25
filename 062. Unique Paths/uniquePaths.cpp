class Solution {
public:
    int uniquePaths(int m, int n) {
        return combination(m+n-2, m-1);
    }
    // C(n,r) = n!/[r!(n-r)!]
    int combination(int n, int r) {
        double result = 1; //big int
        for(int i=1;i<r+1;i++) {
            result = result*(n-r+i)/i;
            // C(6,3) = (1x2x3x...x6)/(1x2x3 x 1x2)
            //        = (4x5x6) / (1x2)
            //        = (n-r+i) / i
        }
        return (int)result;
    }
};