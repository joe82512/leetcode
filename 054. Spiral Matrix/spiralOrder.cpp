class Solution {
public:
    vector<int> spiralOrder(vector<vector<int>>& matrix) {
        int row = matrix.size();
        int col = matrix[0].size();
        vector<int> output;
        int U=0, D=row-1, L=0, R=col-1;
        while (true) {
            // go right
            for (int x=L; x<=R; x++) { output.push_back(matrix[U][x]); }
            U++; //change boundry cause visited
            if (U>D) { break; } //boundry condition
            // go down
            for (int y=U; y<=D; y++) { output.push_back(matrix[y][R]); }
            R--;
            if (R<L) { break; }
            // go left
            for (int x=R; x>=L; x--) { output.push_back(matrix[D][x]); }
            D--;
            if (D<U) { break; }
            // go up
            for (int y=D; y>=U; y--) { output.push_back(matrix[y][L]); }
            L++;
            if (L>R) { break; }
        }

        return output;
    }
};