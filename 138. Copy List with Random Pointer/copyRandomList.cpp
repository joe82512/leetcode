/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* next;
    Node* random;
    
    Node(int _val) {
        val = _val;
        next = NULL;
        random = NULL;
    }
};
*/

class Solution {
public:
    Node* copyRandomList(Node* head) {
        if (!head) {
            return nullptr; //not NULL
        }
        Node* curr = new Node(head->val);
        Node* result = new Node(0, curr);
        unordered_map<Node*, Node*> mp = {{head, result->next}};
        while (head) {
            // next
            if (!head->next) {
                curr->next = nullptr;
            }
            else if (mp.find(head->next)!=mp.end()) {
                curr->next = mp[head->next];
            }
            else {
                curr->next = new Node(head->next->val);
                mp[head->next] = curr->next;
            }

            // random
            if (!head->random) {
                curr->random = nullptr;
            }
            else if (mp.find(head->random)!=mp.end()) {
                curr->random = mp[head->random];
            }
            else {
                curr->random = new Node(head->random->val);
                mp[head->random] = curr->random;
            }

            //step
            head = head->next;
            curr = curr->next;
        }
        return result->next;
    }
};