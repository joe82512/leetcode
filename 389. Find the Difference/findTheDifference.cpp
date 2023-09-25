class Solution {
public:
    char findTheDifference(string s, string t) {
        s += t; //all char
        char output = '\0'; //ascii(0) : null, not 0
        for (auto c:s) { output ^= c; }
        return output;
    }
};