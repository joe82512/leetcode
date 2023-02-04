class Solution {
public:
    bool wordPattern(string pattern, string s) {
        istringstream is(s);
        string word;
        vector<string> list_str;
        while( is>>word ) {  
            list_str.push_back(word);  
        }
        unordered_map<char, string> result;
        vector<string> value;
        int exist_cnt;

        if (list_str.size() != pattern.size()) {
            return false;
        }

        for (int i=0; i<pattern.size(); i++) {
            exist_cnt = result.count(pattern[i]);
            if (exist_cnt > 0) {
                if (result[pattern[i]] != list_str[i]) { //error value
                    return false;
                }
            }
            else {
                result[pattern[i]] = list_str[i];
                exist_cnt = count(value.begin(),value.end(),list_str[i]);
                if (exist_cnt > 0) { //duplicate value
                    return false;
                }
                else {
                    value.push_back(list_str[i]);
                }
            }
        }
        return true;
    }
};