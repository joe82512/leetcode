class Solution {
public:
    int fib(int n) {
        int a = 0, b = 1;
        if (n==0) {return a;} //F(0)
        else if (n==1) {return b;} //F(1)
        for ( int i=2; i<n+1; i++ ) { //F(2)~F(n)
            int temp = b;
            b = a+b; //F(n) = F(n-2)+F(n-1)
            a = temp;
        }
        return b;
    }
};