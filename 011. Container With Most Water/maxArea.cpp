class Solution {
public:
    int maxArea(vector<int>& height) {
        // DP + 2 pointer
        int L = 0;
        int R = height.size()-1;
        int area = 0;
        int res = 0;
        
        while (L < R) {
            area = (R-L)*min(height[R],height[L]);
            res = max(area,res); // DP
            // update to (maybe) large
            if (height[L] > height[R]) { R--; }
            else { L++; }
        }
        return res;
    }
};