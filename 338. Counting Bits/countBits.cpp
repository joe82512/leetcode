class Solution {
public:
    vector<int> countBits(int n) {
        // {0,1,1,2,1,2,2,3,1,2,2,3,2,3,3,4,1,...}
        //  ^ ^   ^       ^               ^
        //  0 1   3       7               15
        vector<int> output = {0};
        for (int i=1; i<n+1; i++) {
            int idx = i/2;
            output.push_back(output[idx]+i%2);
        }
        return output;
    }
};