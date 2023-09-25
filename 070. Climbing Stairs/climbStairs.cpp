class Solution {
public:
    int climbStairs(int n) {
        // maybe from 1 step or 2 step : a0(+2step) + a1(+1step) = a3(+0step)
        // Fibonacci : [1,2,3,5,8, ...]
        int a0 = 0;
        int a1 = 1;
        for (int i=0; i<n; i++) {
            //(a1,a0) = (a1+a0,a1)
            int temp = a0;
            a0 = a1;
            a1 = a1+temp;
        }
        return a1;
    }
};