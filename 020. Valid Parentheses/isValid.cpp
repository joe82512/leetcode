class Solution {
public:
    bool isValid(string s) {
        stack<char> sout;
        unordered_map<char,char> parentheses = {
            {'(',')'},
            {'{','}'},
            {'[',']'}
        };
        for (auto c:s) {
            
            if (parentheses.find(c) != parentheses.end()) {
                sout.push(parentheses[c]);
            }
            else if (sout.empty() or sout.top()!=c) {
                return false;
            }
            else {
                sout.pop();
            }
        };
        return sout.size()==0;
    }
};