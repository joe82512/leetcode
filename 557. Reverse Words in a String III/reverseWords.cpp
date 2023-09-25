class Solution {
public:
    string reverseWords(string s) {
        string output = "", temp;
        istringstream is(s);
        while (is >> temp) {
            reverse(temp.begin(), temp.end());
            output += (temp+" ");
        }
        output.pop_back(); //last space
        return output;
    }
};