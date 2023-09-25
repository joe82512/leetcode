class Solution {
public:
    int numSimilarGroups(vector<string>& strs) {
        vector<bool> visited(strs.size(),false);
        int output = 0; //groups
        for (int i=0; i<strs.size(); i++) { //scan graph tree
            output += DFS(i, strs, visited);
        }
        return output;
    }

    // swap only one time can match(s1==s2)
    bool is_similar(string s1, string s2) {
        int diff_cnt = 0;
        for (int i=0; i<s1.size(); i++) {
            if (s1[i]!=s2[i]) { diff_cnt++; }
            if (diff_cnt>2) { return false; }
        }
        return true;
    }

    // DFS
    int DFS(int idx, vector<string> &strs, vector<bool> &visited) {
        // already used
        if (visited[idx]) { return 0; } //continue, do nothig
        // else, not used
        visited[idx] = true; //used
        for (int i=0; i<strs.size(); i++) { //scan all tree node
            if (!visited[i] && is_similar(strs[idx], strs[i])) {
                DFS(i, strs, visited);
            }
            // else: conitnue, do nothing
        }
        return 1; //group +1
    }
};