class Solution {
public:
    int minimumRounds(vector<int>& tasks) {
        unordered_map<int,int> cnt; //task counter
        for (int num:tasks) { cnt[num] = cnt[num]+1; }

        int res = 0;
        for (auto cnt_item:cnt) {
            int c = cnt_item.second;
            if (c==1) { return -1; }
            if (c%3==0) { res = res+(c/3); } //3*n
            else { res = res+(c/3)+1; } //3*n+1=3*(n-1)+2+2 ; 3*n+2
        }
        
        return res;
    }
};