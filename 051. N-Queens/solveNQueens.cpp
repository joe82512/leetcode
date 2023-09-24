class Solution {
public:
    vector<vector<string>> solveNQueens(int n) {
        vector<vector<string>> result;
        vector<int> qCol(n, -1);
        DFS(0, qCol, result);
        return result;
    }

    void DFS(int row, vector<int>& qCol, vector<vector<string>>& result) {
        int n = qCol.size();
        // full and return out
        if (row == n) {
            vector<string> out(n, string(n,'.')); //create [[...],[...],[...]]
            for (int i=0; i<n; i++) {
                out[i][qCol[i]] = 'Q'; //set 'Q'
            }
            result.push_back(out);
            return;
        }
        // fill up by DFS
        for (int i=0; i<n; i++) {
            qCol[row] = i; //set index
            if (check(qCol, row, i)) { DFS(row+1, qCol, result); }
            //qCol[row] = -1; //initial index
        }
    }

    // fail: same index or diagonal position
    bool check(vector<int>& qCol, int row, int col) {
        for (int i=0; i<row; i++) {
            if (col==qCol[i] || abs(row-i)==abs(col-qCol[i])) {
                return false;
            }
        }
        return true;
    }
};