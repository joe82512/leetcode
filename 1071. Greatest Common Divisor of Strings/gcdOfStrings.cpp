class Solution {
public:
    string gcdOfStrings(string str1, string str2) {
        if (str1.size() > str2.size())
            return gcdOfStrings(str2, str1);

        if (str1.empty())
            return string(str2);

        if (str2.substr(0, str1.size()) != str1)
            return "";

        return gcdOfStrings(str1, str2.substr(str1.size()));
    }
};