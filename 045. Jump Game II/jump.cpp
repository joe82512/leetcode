class Solution {
public:
    int jump(vector<int>& nums) {
        int cnt = 0;
        int idxMaxPosition = 0;
        int resMaxPosition = 0;

        // special case
        if (nums.size()<=1) { return 0; }

        for (int i=0; i<nums.size(); ++i) {
            idxMaxPosition = max(idxMaxPosition, i + nums[i]); //update

            if (i==resMaxPosition) {
                resMaxPosition = idxMaxPosition; //update
                cnt++;
                // if complete
                if (idxMaxPosition >= nums.size()-1) { break; }
            }
        }

        return cnt;
    }
};