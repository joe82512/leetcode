class Solution {
public:
    void rotate(vector<vector<int>>& matrix) {
        int n = matrix.size();
        // vertical transfer
        reverse(matrix.begin(), matrix.end());
        // diagonal transfer
        for (int i=0; i<n; i++) {
            for (int j=i+1; j<n; j++) { //just get upper triangle
                swap(matrix[i][j],matrix[j][i]);
            }
        }
    }
};