class Solution {
public:
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        vector<vector<int>> res_list;
        vector<int> res;
        comb(0,candidates,target,res,res_list);
        return res_list;
    }
    void comb(int idx, vector<int> can, int tar, vector<int> &res, vector<vector<int>> &res_list) {
        // match: output
        if (tar==0) { res_list.push_back(res); }
        // no match: overflow
        else if(tar<0) { return; }
        // no match: fill up
        for(int i=idx; i<can.size(); i++) {
            res.push_back(can[i]); //nums array slice
            comb(i,can,tar-can[i],res,res_list);
            res.pop_back();
        }
    }
};