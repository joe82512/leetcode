class Solution {
public:
    int addDigits(int num) {
        int r = 0;
        // add least weight
        while (num) {
            r = r + (num%10);
            num = num/10; //int
        }
        if (r<10) { return r; }
        else { return addDigits(r); } //again
    }
};