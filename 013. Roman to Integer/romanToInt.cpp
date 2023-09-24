class Solution {
public:
    int romanToInt(string s) {
        unordered_map<char, int> symDict;
        symDict = {
            {'I',1},{'V',5},{'X',10},{'L',50},{'C',100},{'D',500},{'M',1000}
        };
        int res = 0;
        for (int i=0; i<s.length(); i++) {
            res += symDict[s[i]];
            //subtract back
            if (symDict[s[i]] < symDict[s[i+1]]) {
                res -= symDict[s[i]]*2;
            }
        }

        return res;
    }
};