class Solution {
public:
    vector<int> replaceElements(vector<int>& arr) {
        int temp = -1; //initial
        int n = arr.size();
        for (int i=n-1; i>=0; i--) {
            // arr[i],temp = temp,max(arr[i],temp)
            int now_arr = arr[i];
            arr[i] = temp;
            temp = max(now_arr,temp);
        }
        return arr;
    }
};