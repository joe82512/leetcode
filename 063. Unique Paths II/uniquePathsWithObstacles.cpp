class Solution {
public:
    int uniquePathsWithObstacles(vector<vector<int>>& obstacleGrid) {
        int row = obstacleGrid.size();
        int col = obstacleGrid[0].size();
        vector<vector<int>> dp(row,vector<int>(col,0));

        // source point
        if (obstacleGrid[0][0]==0) { dp[0][0] = 1; }
        else { dp[0][0] = 0; }

        // DP
        for (int i=0; i<row; i++) {
            for (int j=0; j<col; j++) {
                // if stuck , avoid path
                if (obstacleGrid[i][j]==1) { dp[i][j] = 0; }
                else {
                    // i=0 Boundary
                    if (i>0) { dp[i][j] = dp[i][j] + dp[i-1][j]; }
                    // j=0 Boundary
                    if (j>0) { dp[i][j] = dp[i][j] + dp[i][j-1]; }
                }  
            }
        }
        return dp[row-1][col-1];
    }
};