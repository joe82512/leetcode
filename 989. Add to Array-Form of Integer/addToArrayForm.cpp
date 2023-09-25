class Solution {
public:
    vector<int> addToArrayForm(vector<int>& num, int k) {
        int idx = num.size()-1;
        int carry = 0;
        int k_num, add;
        // int->vector by LSB shift
        while (idx>=0 or k>0) {
            k_num = k%10;
            k = k/10;
            // num >= k
            if (idx>=0) {
                add = num[idx] + k_num + carry;
                num[idx] = add%10;
            }
            // num < k
            else {
                add = k_num + carry;
                num.insert(num.begin(),add%10);
            }
            carry = add/10;
            idx = idx-1;
        }
        // overflow
        if (carry!=0) { num.insert(num.begin(),carry); }
        return num;
    }
};