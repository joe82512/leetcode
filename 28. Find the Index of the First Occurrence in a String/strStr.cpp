class Solution {
public:
    int strStr(string haystack, string needle) {
        if (haystack.size() < needle.size()) { return -1; }
        else if (haystack == needle) { return 0; }
        //else {} sliding window

        int h_l = haystack.size();
        int n_l = needle.size();
        for (int L=0; L<h_l-n_l+1; ++L) {
            for (int W=0; W<n_l; ++W) {
                if (haystack[L+W] != needle[W]) { break; }
                else if (W==n_l-1) { return L; } //go through
            }
        }
        return -1;
    }
};