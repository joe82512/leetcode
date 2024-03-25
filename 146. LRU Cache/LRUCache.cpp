class LRUCache {
    /*
    # hashmap -> search: O(1)
    # linked-list -> insert: O(1)
    # double linked-list -> insert: O(1) / remove: O(1)
    # combine hashmap + double linked-list
    */
public:
    class Node{
        public: 
            int key;
            int val;
            Node* prev;
            Node* next;

            Node(int key, int val){
                this->key = key;
                this->val = val;
            }
    };

    int cap;
    // double linked-list: cap+2, cause dummy head and dummy tail
    Node* head = new Node(-1, -1);
    Node* tail = new Node(-1, -1);
    // hashmap
    unordered_map<int, Node*> hashmap;

    LRUCache(int capacity) {
        cap = capacity;
        head->next = tail;
        tail->prev = head;
    }
    
    // double linked-list insert
    void insertHead(Node* node) {
        Node* temp;
        temp = head->next;

        node->next = temp;
        node->prev = head;

        temp->prev = node;
        head->next = node;
    }

    // double linked-list remove
    void remove(Node* node) {
        Node* prev_node = node->prev;
        Node* next_node = node->next;

        prev_node->next = next_node;
        next_node->prev = prev_node;
    }

    int get(int key) {
        // if exist, move to front
        if (hashmap.find(key) != hashmap.end()) {
            Node* node = hashmap[key];
            int value = node->val;
            // delete
            hashmap.erase(key);
            remove(node);
            // combine, move to front
            insertHead(node);
            hashmap[key] = head->next; //not head
            return value;
        }
        else { return -1; }
    }
    
    void put(int key, int value) {
        // step1. delete if update
        if (hashmap.find(key) != hashmap.end()) {
            Node* node = hashmap[key];
            hashmap.erase(key);
            remove(node);
        }

        // step1. delete tail.prev if overflow
        if(hashmap.size() == cap) {
            hashmap.erase(tail->prev->key); //not tail
            remove(tail->prev);
        }

        // step2. combine, move to front
        insertHead(new Node(key, value));
        hashmap[key] = head->next;
    }
};

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache* obj = new LRUCache(capacity);
 * int param_1 = obj->get(key);
 * obj->put(key,value);
 */