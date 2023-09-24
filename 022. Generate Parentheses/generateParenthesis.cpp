class Solution {
public:
    vector<string> generateParenthesis(int n) {
        vector<string> res{};
        DFS(0,0,"",n,res);
        return res;
    }
    void DFS(int L, int R, string s, int &n, vector<string> &res) {
        // full char , return
        if (s.length()==n*2) {
            res.push_back(s);
            return;
        }
        // can go left if left step times not full
        if (L<n) { DFS(L+1, R, s+"(", n, res); }
        // can go right if left already step
        if (L>R) { DFS(L, R+1, s+")", n, res); }
    }
};