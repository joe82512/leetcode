class Solution {
public:
    bool validPath(int n, vector<vector<int>>& edges, int source, int destination) {
        unordered_map<int,vector<int>> path;
        for (vector<int> e:edges) {
            if (path.find(e[0])!=path.end()) {
                path[e[0]].push_back(e[1]);
            }
            else {
                path[e[0]] = {e[1]};
            }
            if (path.find(e[1])!=path.end()) {
                path[e[1]].push_back(e[0]);
            }
            else {
                path[e[1]] = {e[0]};
            }
        }

        queue<int> q;
        q.push(source);

        vector<bool> visited(n);
        while (!q.empty()) {
            int curr = q.front();
            q.pop();
            if (curr==destination) {
                return true;
            }
            else if (path.find(curr)!=path.end() & !visited[curr]) {
                for (int pv:path[curr]) {
                    q.push(pv);
                }                
            }
            visited[curr] = true;
        }
        return false;
    }
};