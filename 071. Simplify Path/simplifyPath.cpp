class Solution {
public:
    string simplifyPath(string path) {
        stack<string> st;
        int i = 0;
        int n = path.length();
        while ( i < n ) {
            // slice string
            string s = "";
            while ( i < n ) {
                if ( path[i]=='/' ) { break; }
                // string temp;
                // char c = path[i];
                // temp = c;
                // s = s + temp;
                s = s + path[i];
                i++;
            }
            // check relative path
            if ( s==".." ) { if (!st.empty()) {st.pop();} }
            else if ( s!="." && s!="" ) { st.push(s); }
            // next string
            i++;
        }
        // join string
        string newPath = "";
        while (!st.empty()) { 
            string s = st.top();
            st.pop();
            newPath =  "/" + s + newPath;
        }
        // return
        if (newPath=="") { return "/"; }
        else { return newPath; }
    }
};