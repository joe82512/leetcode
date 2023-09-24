class Solution {
public:
    bool isValid(string s) {
        stack<char> sout;
        unordered_map<char,char> parentheses = {
            {'(',')'},
            {'{','}'},
            {'[',']'}
        };
        for (char c:s) {
            // find in hashmap -> push
            if (parentheses.find(c) != parentheses.end()) {
                sout.push(parentheses[c]);
            }
            // other char or not match
            else if (sout.empty() or sout.top()!=c) {
                return false;
            }
            // match and popup(-1)
            else {
                sout.pop();
            }
        };
        return sout.size()==0;
    }
};