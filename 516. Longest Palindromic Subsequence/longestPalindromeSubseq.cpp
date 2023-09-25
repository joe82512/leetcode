class Solution {
public:
    int longestPalindromeSubseq(string s) {
        int n = s.size();
        vector<vector<int>> dp(n, vector(n,0)); // ixj->nxn
        /*
        i: L(head) <- R(tail) / j: up(head) -> down(tail)
        
        <case 1> i>j : 0 (triangular matrix)
        <case 2> i==j : 1 (diagonal , initial)
        <case 3> s[i]==s[j] : both move , count +2
        <case 4> s[i]!=s[j] : move i or move j , but not count
        */
        
        for (int i=n-1; i>=0; i--) { //0~n
            dp[i][i] = 1;
            for (int j=i+1; j<n; j++) { //0~i-1
                if (s[i]==s[j]) { dp[i][j] = 2 + dp[i+1][j-1]; }
                else            { dp[i][j] = max(dp[i+1][j],dp[i][j-1]); }
            }
        }
        return dp[0][n-1];
    }
};