class Solution {
public:
    bool canPlaceFlowers(vector<int>& flowerbed, int n) {
        if (n==0) { return true; }
        int cnt = 0; //planted counter
        int len = flowerbed.size();
        for (int i=0; i<len; i++) {
            // empty and adjacent empty
            if ( (i==0||flowerbed[i-1]==0) && (flowerbed[i]==0) && (i==len-1||flowerbed[i+1]==0) ) {
                flowerbed[i] = 1; //planted
                cnt += 1;
                if (cnt==n) { return true; } //cnt>=n , early break
            }
        }

        return false;
    }
};