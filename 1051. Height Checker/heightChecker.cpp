class Solution {
public:
    int heightChecker(vector<int>& heights) {
        // create spec
        vector<int> sort_heights = heights;
        sort(sort_heights.begin(),sort_heights.end());
        // compare spec
        int not_match = 0;
        for (int i=0; i<heights.size(); i++) {
            if (sort_heights[i]!=heights[i]) { not_match += 1 ; }
        }
        return not_match;
    }
};