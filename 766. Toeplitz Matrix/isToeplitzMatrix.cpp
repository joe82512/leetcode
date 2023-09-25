class Solution {
public:
    bool isToeplitzMatrix(vector<vector<int>>& matrix) {
        int row=matrix.size(), col=matrix[0].size();
        for (int i=1; i<row; i++) {
            for (int j=1; j<col; j++) {
                // top-left to bottom-right
                if (matrix[i][j]!=matrix[i-1][j-1]) { return false; }
            }
        }
        return true;
    }
};