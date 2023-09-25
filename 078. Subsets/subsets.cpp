class Solution {
public:
    vector<vector<int>> subsets(vector<int>& nums) {
        vector<vector<int>> result = {{}};
        // brute force
        for (auto num:nums) { //get element
            vector<vector<int>> temps;
            temps = result;
            for (auto temp:temps) {
                temp.push_back(num); //all vector append element
                result.push_back(temp); //update all vector
            }
        }
        return result;
    }
};