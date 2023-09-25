class Solution {
public:
    vector<vector<int>> combine(int n, int k) {
        vector<int> res;
        vector<vector<int>> res_list;
        dfs(1,n,k,res,res_list);
        return res_list;
    }

    void dfs(int idx, int &n, int &k, vector<int> &res, vector<vector<int>> &res_list) {
        // full and return
        if (res.size()==k) {
            res_list.push_back(res);
            return;
        }
        // fill up
        else {
            for (int i=idx;i<n+1;i++) {
                res.push_back(i);
                dfs(i+1,n,k,res,res_list);
                res.pop_back();
            }
        }
    }
};