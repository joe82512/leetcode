class Solution {
public:
    vector<int> sortArray(vector<int>& nums) {
        int c_len = 50000+1-(-50000);
        vector<int> count(c_len);
        int idx = 0;
        vector<int> res(nums.size());
        for (auto n:nums) {
            count[n+50000] += 1;
        }
        for (int i=0; i<count.size(); i++) {
            if (count[i] != 0) {
                while (count[i] > 0) {
                    count[i] -= 1;
                    res[idx] = i-50000;
                    idx += 1;
                }
            }
        }
        return res;
    }
};