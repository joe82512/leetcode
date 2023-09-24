class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        // group string
        unordered_map<string, vector<string>> group;
        for (string s:strs) {
            string sort_s = s;
            sort(sort_s.begin(), sort_s.end());
            group[sort_s].push_back(s); //auto empty value initial
        }
        // get value
        vector<vector<string>> output;
        for (auto item:group) {
            output.push_back(item.second);
        }

        return output;
    }
};