class Solution {
public:
    vector<int> answerQueries(vector<int>& nums, vector<int>& queries) {
        sort(begin(nums), end(nums));
        vector<int> listSize;
        int k = 0;
        for (int n:nums) {
            k += n;
            listSize.push_back(k);
        }

        vector<int> res;
        for (int q:queries) {
            int idx = upper_bound(begin(listSize), end(listSize), q) - begin(listSize);
            res.push_back(idx);
        }
        return res;
    }
};