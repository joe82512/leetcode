class Solution {
public:
    vector<int> findDisappearedNumbers(vector<int>& nums) {
        vector<int> v(nums.size(),0);
        vector<int> r;
        for(int i=0;i<nums.size();i++)
        {
            v[nums[i]-1] = 1;
        }
        for(int i=0;i<nums.size();i++)
        {
            if(v[i]==0)
            {
                r.push_back(i+1);
            }
        }
        return r;

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