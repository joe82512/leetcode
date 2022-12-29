class Solution {
public:
    vector<vector<int>> res_list;
    vector<int> res;
    void dfs(int idx, int n, int k) {
        if (res.size()==k) {
            res_list.push_back(res);
            return;
        }
        else {
            for (int i=idx;i<n+1;i++) {
                res.push_back(i);
                dfs(i+1,n,k);
                res.pop_back();
            }
        }
    }
    
    vector<vector<int>> combine(int n, int k) {
        dfs(1,n,k);
        return res_list;
    }
};