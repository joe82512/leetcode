class Solution {
public:
    int maxDistance(vector<vector<int>>& grid) {
        // sol : DP + BFS
        
        // get land (1) graph
        queue<vector <int>> q;
        int n = grid.size();
        for (int i=0; i<n; i++) {
            for (int j=0; j<n ;j++) {
                if (grid[i][j]==1) { q.push({i,j,0}); }
            }
        }

        // all 1 or all 0
        if (q.size()==n*n || q.size()==0) { return -1; }

        // next step
        vector<vector<int>> directions = {{0,1},{1,0},{-1,0},{0,-1}};
        
        // DP
        int area = 1;
        // BFS
        while (!q.empty()) {
            vector<int> p = q.front();
            int i = p[0], j = p[1], d = p[2];
            q.pop();
            for (auto dirs:directions) {
                // next step
                int next_i = i + dirs[0], next_j = j + dirs[1];
                // Boundary Condition ; Note: n>next_i>=0 error
                if ( n>next_i && next_i>=0 && n>next_j && next_j>=0) {
                    // calculate water (0) distance
                    if ( grid[next_i][next_j]==0) {
                        q.push({next_i,next_j,d+1});
                        grid[next_i][next_j] = d+1; //DP
                        area = max(area,grid[next_i][next_j]); //DP
                    }
                }
            }
        }
        return area;
    }
};