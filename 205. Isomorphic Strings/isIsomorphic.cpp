class Solution {
public:
    bool isIsomorphic(string s, string t) {
        if (s.length()!=t.length()) { return false; }
        // else
        // 2 map for one <-> one , multi <-> one fail
        unordered_map<char,char> map_st, map_ts;
        for (int i=0; i<s.length(); i++) {
            if ( map_st[s[i]] && map_st[s[i]]!=t[i]) { return false; }
            if ( map_ts[t[i]] && map_ts[t[i]]!=s[i]) { return false; }
            // else
            map_st[s[i]] = t[i];
            map_ts[t[i]] = s[i];
        }
        return true;
    }
};