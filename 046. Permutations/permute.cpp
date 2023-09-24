class Solution {
public:
    vector<vector<int>> permute(vector<int>& nums) {
        vector<vector<int>> res;
        vector<int> path;
        vector<int> visited(nums.size(), 0);
        DFS(nums, visited, path, res);
        return res;
    }

    void DFS(vector<int> &nums, vector<int> &visited, vector<int> &path, vector<vector<int>> &res) {
        // full and return
        if (path.size() == nums.size()) {
            res.push_back(path);
            return;
        }
        
        for (int i=0; i<nums.size(); i++) {
            // already used
            if (visited[i] == 1) { continue; }
            // DFS
            else {
                path.push_back(nums[i]);
                visited[i] = 1;
                DFS(nums, visited, path, res);
                path.pop_back();
                visited[i] = 0;
            }
        }
    }
};