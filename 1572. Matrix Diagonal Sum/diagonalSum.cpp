class Solution {
public:
    int diagonalSum(vector<vector<int>>& mat) {
        int r = 0;
        int n = mat.size();
        for (int i=0; i<n; i++) {
            // repeat : two diagonal cross 
            if (n%2==1 && i==(n-1)/2) { r += mat[i][i]; }
            // primary & secondary diagonal
            else { r += (mat[i][i]+mat[i][n-i-1]); }
        }
        return r;
    }
};