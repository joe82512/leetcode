class Solution {
public:
    bool detectCapitalUse(string word) {
        // count upper
        int cnt = 0;
        for (int i=0; i<word.size(); i++) {
            if (isupper(word[i])) { cnt++; }
        }
        // all upper
        if (isupper(word[0]) && cnt==word.size()) { return true; }
        // first upper
        else if (isupper(word[0]) && cnt==1) { return true; }
        // all lower
        else if (cnt==0) { return true; }
        // else
        return false;
    }
};