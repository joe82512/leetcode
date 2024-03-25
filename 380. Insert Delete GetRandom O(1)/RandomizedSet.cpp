class RandomizedSet {
    // global
    unordered_map<int,int> mp; //{val: idx}, not ordered_map
    vector<int> vals;

public:
    RandomizedSet() {
        
    }
    
    bool insert(int val) {
        if (mp.find(val)!=mp.end()) { return false; } //exist
        //else{}
        mp[val] = vals.size(); //last index
        vals.push_back(val);
        return true;
    }
    
    bool remove(int val) {
        if (mp.find(val)==mp.end()) { return false; } //not found
        //else{}
        // search index
        auto it = mp.find(val); //hashmap search: O(1)
        // copy and cover last as target -> unstable
        vals[it->second] = vals.back();
        mp[vals[it->second]] = it->second;
        // delete last
        mp.erase(val);
        vals.pop_back();
        return true;
    }
    
    int getRandom() {
        return vals[rand() % vals.size()];
    }
};

/**
 * Your RandomizedSet object will be instantiated and called as such:
 * RandomizedSet* obj = new RandomizedSet();
 * bool param_1 = obj->insert(val);
 * bool param_2 = obj->remove(val);
 * int param_3 = obj->getRandom();
 */