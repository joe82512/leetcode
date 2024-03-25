class Solution {
public:
    bool wordBreak(string s, vector<string>& wordDict) {
        // dp[idx]=combine pass/fail, idx=string index
        vector<bool> dp(s.length()+1, false);
        dp[0] = true;

        for (int i=1; i<s.length()+1; ++i) { //string index
            for (int j=0; j<i; ++j) { //s[0:j], s[j:i] both pass
                if (dp[j] && find(wordDict.begin(), wordDict.end(), s.substr(j,i-j))!=wordDict.end()) {
                    dp[i] = true;
                    break;
                }
            }
        }

        return dp[s.length()];
    }
};