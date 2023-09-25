class Solution {
public:
    int minimumTotal(vector<vector<int>>& triangle) {
        // DP
        int row = triangle.size();
        for (int i=row-2; i>=0; i--) { //last 2 row -> top row
            int col = triangle[i].size();
            for (int j=0; j<col; j++) { //add next row
                triangle[i][j] += min(triangle[i+1][j], triangle[i+1][j+1]); //column neighbor
            }
        }
        return triangle[0][0];
    }
};