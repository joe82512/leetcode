class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        // empty
        if (matrix.size()==0) { return false; }
        else if (matrix[0].size()==0) { return false; }
        // else
        int m = matrix.size();
        int n = matrix[0].size();
        int L = 0, R = m*n-1; //flat to 1D

        while (L<=R) {
            int mid = L + (R-L)/2;
            int row = mid/n; //flat to 1D
            int col = mid%n; //flat to 1D
            // binary search
            if (matrix[row][col] == target) { return true; }
            else if (matrix[row][col] < target) { L = mid + 1; }
            else { R = mid - 1; }
        }

        return false;
    }
};