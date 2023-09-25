// The API isBadVersion is defined for you.
// bool isBadVersion(int version);

class Solution {
public:
    int firstBadVersion(int n) {
        // binary search tree
        int L = 1, R = n; // add 1
        while (L < R) {
            int mid = L + (R-L)/2;
            if (isBadVersion(mid)) { R = mid; }
            else { L = mid + 1; }
        }
        return L;
    }
};