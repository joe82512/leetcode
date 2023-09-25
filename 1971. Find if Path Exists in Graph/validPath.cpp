class Solution {
public:
    bool validPath(int n, vector<vector<int>>& edges, int source, int destination) {
        // create path map
        unordered_map<int,vector<int>> path;
        for (vector<int> e:edges) {
            path[e[0]].push_back(e[1]);
            path[e[1]].push_back(e[0]);
        }

        // BFS + visited
        queue<int> q;
        q.push(source);
        vector<bool> visited(n); //avoid same path

        while (!q.empty()) {
            int now_e = q.front();
            q.pop();
            // goal
            if (now_e==destination) { return true; }
            // on the way , avoid same way
            else if (path.find(now_e)!=path.end() & !visited[now_e]) {
                for (int next_e:path[now_e]) {
                    q.push(next_e);
                }                
            }
            visited[now_e] = true; //sign way
        }
        return false; //not goal
    }
};