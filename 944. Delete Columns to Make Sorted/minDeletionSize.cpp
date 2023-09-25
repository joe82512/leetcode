class Solution {
public:
    int minDeletionSize(vector<string>& strs) {
        int r = 0;
        int row = strs.size();
        int col = strs[0].length();
        // vertical scan
        for (int j=0; j<col; j++) {
            for (int i=1; i<row; i++) {
                // check sort
                if (strs[i][j] < strs[i-1][j]) { r++; break; }
            }
        }
        return r;
    }
};