// count sort
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



// merge sort
class Solution {
public:
    vector<int> sortArray(vector<int>& nums) {
     	mergeSort(nums, 0, nums.size()-1);
    	return nums;
    }

    void mergeSort(vector<int>& nums, int start, int end) {
    	if (start >= end) { return; }
    	int mid = (start+end) / 2;
        // slice vector
    	mergeSort(nums, start, mid);
    	mergeSort(nums, mid+1, end);
        // combine
    	merge(nums, start, mid, end);
    }

    void merge(vector<int>& nums, int start, int mid, int end) {
        // recover vector (combine)
        vector<int> temp(end - start + 1);
        int i = start, j = mid+1, k = 0;
        while (i<=mid && j<=end) {
        	if (nums[i]<nums[j]) { temp[k++] = nums[i++]; }
        	else                 { temp[k++] = nums[j++]; } 
        }
        while (i<=mid) { temp[k++] = nums[i++]; }
        while (j<=end) { temp[k++] = nums[j++]; }
        // update on nums
        for (int idx=0; idx<temp.size(); idx++) { nums[idx+start] = temp[idx]; }
    }
};