class Solution {
public:
    vector<vector<int>> transpose(vector<vector<int>>& matrix) {
        int m = matrix.size();
        int n = matrix[0].size();
        // mxn -> nxm
        vector<vector<int>> output;
        vector<int> col(m);
        output.resize(n,col);
        // Transpose
        for (int i=0; i<m; i++) {
            for (int j=0; j<n; j++) {
                output[j][i] = matrix[i][j];
            }
        }
        return output;
    }
};