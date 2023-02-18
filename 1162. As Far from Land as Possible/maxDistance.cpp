class Solution {
public:
    int maxDistance(vector<vector<int>>& grid) {
        queue<vector <int>> q;
        int n = grid.size();
        for (int i=0; i<n; i++) {
            for (int j=0; j<n ;j++) {
                if (grid[i][j]==1) {
                    q.push({i,j,0});
                }
            }
        }

        if (q.size()==n*n || q.size()==0) {
            return -1;
        }

        vector<int> p;
        vector<vector<int>> directions = {{0,1},{1,0},{-1,0},{0,-1}};
        int area = 1;
        while (!q.empty()) {
            p = q.front();
            q.pop();
            for (auto dirs:directions) {
                int next_i = p[0] + dirs[0];
                int next_j = p[1] + dirs[1];
                if ( n>next_i && next_i>=0 && n>next_j && next_j>=0 && grid[next_i][next_j]==0) { //n>next_i>=0 error
                    q.push({next_i,next_j,grid[p[0]][p[1]]+1});
                    grid[next_i][next_j] = grid[p[0]][p[1]]+1;
                    area = max(area,grid[p[0]][p[1]]); //why?
                }
            }
        }
        return area;
    }
};