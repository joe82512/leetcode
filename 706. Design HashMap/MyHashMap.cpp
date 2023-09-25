class MyHashMap {
public:
    vector<int> data;
    
    MyHashMap() {
        data.resize(1e6+1, -1); //initial
    }
    
    void put(int key, int value) {
        data[key] = value;
    }
    
    int get(int key) {
        return data[key]; //-1:not found
    }
    
    void remove(int key) {
        data[key] = -1; //-1:not found
    }
};

/**
 * Your MyHashMap object will be instantiated and called as such:
 * MyHashMap* obj = new MyHashMap();
 * obj->put(key,value);
 * int param_2 = obj->get(key);
 * obj->remove(key);
 */