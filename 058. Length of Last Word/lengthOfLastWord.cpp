class Solution {
public:
    int lengthOfLastWord(string s) {
        int temp_len = 0;
        int idx = s.length()-1;

        // backend to word
        while (idx>=0 && isspace(s[idx])) {
            idx--;
        }
        // calculate word length
        while (idx>=0 && !isspace(s[idx])) {
            idx--;
            temp_len++;
        }

        return temp_len;
    }
};