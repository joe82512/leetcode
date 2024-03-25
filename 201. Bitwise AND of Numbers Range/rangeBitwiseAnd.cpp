class Solution {
public:
    int rangeBitwiseAnd(int left, int right) {
        while (right > left) {
            right = right & (right-1); //反著做
        }
        return right;
    }
};