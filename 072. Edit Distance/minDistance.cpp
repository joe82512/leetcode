class Solution {
public:
    int minDistance(string word1, string word2) {
        int m = word1.length(); //Y
        int n = word2.length(); //X
        // dp[i][j] := min
        // Of operations to convert word1[0..i) to word2[0..j)
        vector<vector<int>> dp(m+1,vector<int>(n+1,0));

        // boundary initial
        for (int i=1; i<m+1; i++) { dp[i][0] = i; } //word1
        for (int j=1; j<n+1; j++) { dp[0][j] = j; } //word2
        // normal
        for (int i=1; i<m+1; i++) {
            for (int j=1; j<n+1; j++) {
                // same : no operation , then go next
                if (word1[i-1]==word2[j-1]) { dp[i][j] = dp[i-1][j-1]; }
                // replace / delete / insert : operate +1
                else { dp[i][j] = min({dp[i-1][j-1], dp[i-1][j], dp[i][j-1]}) +1; }
                //                       replace      delete      insert
            }
        }

        return dp[m][n];
    }
    /*
    Replace (i++,j++) / Delete (i++) / Insert (j++)

    < example 1 >
       r  o  s 
    h  R  D    
    o  I  dp    
    r          
    s          
    e          
    */
};