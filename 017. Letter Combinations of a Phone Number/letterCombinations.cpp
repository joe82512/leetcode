class Solution {
public:
    vector<string> letterCombinations(string digits) {
        unordered_map<char, vector<string>> numDict; //string "" , char ''
        numDict = {
            {'2',{"a","b","c"}},
            {'3',{"d","e","f"}},
            {'4',{"g","h","i"}},
            {'5',{"j","k","l"}},
            {'6',{"m","n","o"}},
            {'7',{"p","q","r","s"}},
            {'8',{"t","u","v"}},
            {'9',{"w","x","y","z"}}
        };

        // empty input
        if (digits=="") { return {}; }
        // input
        vector<string> output{""}; //must initial
        for (char digit:digits) {
            vector<string> temp;
            // Brute Force
            for (const string &s:output) {
                for (string num:numDict[digit]) {
                    temp.push_back(s+num);
                }
            }
            output.swap(temp); //output = temp
        }
        return output;
    }
};