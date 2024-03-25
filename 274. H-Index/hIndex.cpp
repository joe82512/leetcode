class Solution {
public:
    int hIndex(vector<int>& citations) {
        // ref: http://tul.blog.ntu.edu.tw/archives/2485

        // 倒序
        sort(citations.begin(), citations.end(), greater<int>());

        // search
        int total_c = citations.size();
        for (int i=0; i<total_c; ++i) {
            if ( i >= citations[i] ) { return i; }
        }

        // not found
        return total_c;
    }
};