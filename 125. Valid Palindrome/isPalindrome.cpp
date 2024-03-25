class Solution {
public:
    bool isPalindrome(string s) {
        int L = 0;
        int R = s.length()-1;

        char c_L = s[L];
        char c_R = s[R];
        while (L<R) {
            c_L = s[L];
            c_R = s[R];
            
            if (!isalnum(s[L])) { ++L; }
            else if (!isalnum(s[R])) { --R; }
            else if (tolower(s[L]) != tolower(s[R]) ) { return false; }
            else { ++L; --R; }
        }
        return true;
    }
};