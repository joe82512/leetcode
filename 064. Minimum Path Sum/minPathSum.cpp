class Solution {
public:
    int minPathSum(vector<vector<int>>& grid) {
        // dp
        int row = grid.size();
        int col = grid[0].size();

        for (int r=0; r<row; r++) {
            for (int c=0; c<col; c++) {
                // origin
                if (r==0 && c==0) { grid[r][c] = grid[r][c]; }
                // boundary initial
                else if (r==0) { grid[r][c] += grid[r][c-1]; }
                else if (c==0) { grid[r][c] += grid[r-1][c]; }
                // others
                else {  grid[r][c] += min(grid[r-1][c], grid[r][c-1]); }
            }
        }

        return grid[row-1][col-1];
    }
};