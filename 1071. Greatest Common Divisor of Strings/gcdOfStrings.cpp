class Solution {
public:
    string gcdOfStrings(string str1, string str2) {
        /* 輾轉相除法 */

        // swap for keep str1 < str2
        if (str1.size() > str2.size()) { return gcdOfStrings(str2, str1); }
        // if str1 end
        if (str1.empty()) { return string(str2); }
        // str1 check str2[0:i]
        if (str2.substr(0, str1.size()) != str1) { return ""; }
        // recursion : (str1,str2[i:end])
        return gcdOfStrings(str1, str2.substr(str1.size()));
    }
};