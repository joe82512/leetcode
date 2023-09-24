class Solution {
public:
    bool isPalindrome(int x) {
        if (x < 0) { return false; }
        else {
            string str_x = to_string(x);
            string re_x = str_x;
            reverse(re_x.begin(),re_x.end());
            if (str_x == re_x) { return true; }
            else { return false; }
        }
    }
};