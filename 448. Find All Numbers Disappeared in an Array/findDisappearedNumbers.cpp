class Solution {
public:
    vector<int> findDisappearedNumbers(vector<int>& nums) {
        // count num
        vector<int> cnt(nums.size(),0);
        for(int i=0; i<nums.size(); i++) {
            cnt[nums[i]-1] = 1;
        }
        // check 0
        vector<int> output;
        for(int i=0; i<nums.size(); i++) {
            if(cnt[i]==0) { output.push_back(i+1); }
        }
        return output;

        /* ####### slower sol. #######
        set<int> s1;
        set<int> s2(nums.begin(), nums.end());;
        for (int i=0;i<nums.size();i++) {
            s1.insert(i+1);
        }
        set<int> s3;
        vector<int> v;
        set_difference(s1.begin(), s1.end(), s2.begin(), s2.end(), inserter(s3,s3.begin()));
        v.assign(s3.begin(), s3.end());
        
        // for (auto i: v) {
        //     cout << i << '';
        // }            
        
        return v;
        */
    }
};