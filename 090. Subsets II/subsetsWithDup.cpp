class Solution {
public:
    vector<vector<int>> subsetsWithDup(vector<int>& nums) {
        //avoid same element
        sort(nums.begin(),nums.end());
        set<vector<int>> result = {{}};
        // brute force
        for (auto num:nums) { //get element
            set<vector<int>> temps;
            temps = result;
            for (auto temp:temps) {
                temp.push_back(num); //all vector append element
                result.insert(temp);
            }
        }
        vector<vector<int>> output;
        output.assign(result.begin(), result.end()); //set->vector
        return output;
    }
};