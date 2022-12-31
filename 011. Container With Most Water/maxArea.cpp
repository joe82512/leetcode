class Solution {
public:
    int maxArea(vector<int>& height) {
        int left = 0;
        int right = height.size()-1;
        int area = 0;
        int res = 0;
        
        while (left < right) {
            area = (right-left) * min(height[right],height[left]);
            res = max(area,res);
            if (height[left] > height[right]) {
                right -= 1;
            }
            else {
                left += 1;
            }
        }
        return res;
    }
};