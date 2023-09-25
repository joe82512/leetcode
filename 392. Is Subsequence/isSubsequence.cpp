class Solution {
public:
    bool isSubsequence(string s, string t) {
        // Boundary condition
        if (s.length()>t.length()) { return false; }
        else if (s.length()==0) { return true; }
        // else : two pointer
        int ps = 0;
        for (int pt=0; pt<t.length(); pt++) {
            // check
            if ( ps<=s.length()-1 && s[ps]==t[pt] ) { ps++; }
        }
        return (ps ==s.length());
    }
};