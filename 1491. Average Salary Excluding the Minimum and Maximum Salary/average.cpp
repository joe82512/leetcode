class Solution {
public:
    double average(vector<int>& salary) {
        // clean data
        sort(salary.begin(),salary.end());
        salary.erase(salary.begin());
        salary.pop_back();
        // average
        double r = 0;
        for (auto s:salary) { r += s; }
        return r/salary.size();
    }
};