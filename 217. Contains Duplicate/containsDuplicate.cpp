class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        unordered_set<int> numSet; //set without multi-element
        for (auto num:nums) {
            // check same element
            if(numSet.find(num) != numSet.end()){ return true; }
            numSet.insert(num);
        }
        return false;
    }
};