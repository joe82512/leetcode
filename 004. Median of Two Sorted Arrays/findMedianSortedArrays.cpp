class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        if (nums1.size() > nums2.size()) { swap(nums1,nums2); }
        const int n1 = nums1.size(); //small
        const int n2 = nums2.size(); //large
        const int idx = (n1+n2+1)/2; //total half idx

        int L = 0; //L of nums1&nums2 , init of nums1
        int R = n1; //R of nums1&nums2 , init of nums1
        while (L < R) {
            const int mid1 = L + (R-L)/2; //middle of nums1
            const int mid2 = idx - mid1; //middle of nums2
            // update LR
            if (nums1[mid1] < nums2[mid2-1]) { L = mid1 + 1; }
            else { R = mid1; }
        }

        const int mid1 = L;
        const int mid2 = idx - L;
       
        const int c1 = max(mid1 <= 0 ? INT_MIN : nums1[mid1 - 1],  //L of nums1
                           mid2 <= 0 ? INT_MIN : nums2[mid2 - 1]); //L of nums2
 
        const int c2 = min(mid1 >= n1 ? INT_MAX : nums1[mid1],  //R of nums1
                           mid2 >= n2 ? INT_MAX : nums2[mid2]); //R of nums2

        // return
        if ((n1 + n2) % 2 == 1) { return c1; } //odd
        else { return (c1+c2)*0.5; } //even

    }
};