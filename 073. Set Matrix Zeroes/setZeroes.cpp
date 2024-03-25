class Solution {
public:
    void setZeroes(vector<vector<int>>& matrix) {
        int row = matrix.size();
        int col = matrix[0].size();
        vector<vector<int>> zeros;
        // scan all
        vector<int> zero_pos(2,0); //{0,0}
        for (int i=0; i<row; ++i) {
            for (int j=0; j<col; ++j) {
                if (matrix[i][j]==0) {
                    zero_pos = {i,j};
                    zeros.push_back(zero_pos);
                }
            }
        }
        // replace after scan
        for (auto zero:zeros) {
            // cout << zero[0] << zero[1] << endl;
            for (int i=0; i<row; ++i) {
                matrix[i][zero[1]] = 0;
            }
            for (int j=0; j<col; ++j) {
                matrix[zero[0]][j] = 0;
            }
        }
    }
};