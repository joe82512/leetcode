class Solution {
public:
    int numEnclaves(vector<vector<int>>& grid) {
        queue<vector<int>> q;
        int output = 0;
        int row = grid.size();
        int col = grid[0].size();
        
        // create : total lands & initial step (roots)
        for (int i=0; i<row; i++) {
            for (int j=0; j<col; j++) {
                // total lands
                output += grid[i][j];
                // init step : boundary
                if (i==0 || i==row-1 || j==0 || j==col-1) { q.push({i,j}); }
            }
        }

        // BFS
        while (!q.empty()) {
            vector<int> step = q.front();
            int i=step[0], j=step[1];
            q.pop();
            if ( row>i && i>=0 && col>j && j>=0 && grid[i][j]==1) {
                // visited
                grid[i][j]=0; output--;
                // next step
                q.push({i+1,j});
                q.push({i-1,j});
                q.push({i,j+1});
                q.push({i,j-1});
            }
        }
        return output;
    }
};