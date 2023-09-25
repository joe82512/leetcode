class Solution {
public:
    bool wordPattern(string pattern, string s) {
        unordered_map<char, string> patMap;
        istringstream in(s);
        int i = 0, n = pattern.size();

        for (string word; in >> word; i++) {
            // size not match
            if (i > n) { return false; }
            // pat exist
            if (patMap.count(pattern[i])) {
                if (patMap[pattern[i]] != word) { return false; }
            }
            // pat not exist
            else {
                // word collision
                for (auto pat:patMap) {
                    if (pat.second == word) { return false; }
                }
                patMap[pattern[i]] = word;
            }
        }
        return (i == n);
    }
};