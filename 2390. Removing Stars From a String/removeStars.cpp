class Solution {
public:
    string removeStars(string s) {
        string st=""; //string as stack
        for (char c:s) {
            if (c=='*') { st.pop_back(); }
            else { st.push_back(c); }
        }
        return st;
    }
};