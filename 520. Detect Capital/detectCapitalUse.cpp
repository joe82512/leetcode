class Solution {
public:
    bool detectCapitalUse(string word) {
        int cnt = 0;
        for (int i=0; i<word.size(); i++) {
            if (isupper(word[i])) {
                cnt++;
            }
        }

        if (isupper(word[0])) {
            if (cnt==1 || cnt==word.size()) {
                return true;
            }
        }
        else {
            if (cnt==0) {
                return true;
            }
        }
        return false;
    }
};