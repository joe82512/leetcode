class Solution {
public:
    string mergeAlternately(string word1, string word2) {
        int n1 = word1.length();
        int n2 = word2.length();
        int n = max(n1,n2); //get loop times
        
        string s = "";
        for (int i=0; i<n; i++) {
            if (i<n1) { s = s + word1[i]; } //add if char exist
            if (i<n2) { s = s + word2[i]; }
        }

        return s;
    }
};