class Solution {
public:
    bool isAnagram(string s, string t) {
        // sort String
        /*
        sort(s.begin(), s.end(), less<char>());
        sort(t.begin(), t.end(), less<char>());
        return (s==t);
        */
        // count sort
        vector<int> vec1(26,0), vec2(26,0);
        for(int i=0; i<s.size(); i++){ vec1[s[i]-'a']++; }
        for(int i=0; i<t.size(); i++){ vec2[t[i]-'a']++; }
        return (vec1 == vec2);
    }
};