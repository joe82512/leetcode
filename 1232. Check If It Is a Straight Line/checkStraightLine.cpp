class Solution {
public:
    bool checkStraightLine(vector<vector<int>>& coordinates) {
        int n = coordinates.size();
        // point 0~2 , always true
        if (n<=2) { return true; }
        // else
        int dx = coordinates[1][0]-coordinates[0][0];
        int dy = coordinates[1][1]-coordinates[0][1];
        for (int i=2; i<n; i++) {
            int dx2 = coordinates[i][0]-coordinates[0][0];
            int dy2 = coordinates[i][1]-coordinates[0][1];
            // avoid n/0
            if (dx*dy2 != dy*dx2) { return false; }
        }
        // all match
        return true;
    }
};