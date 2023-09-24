/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        // create vale array
        vector<int> arr{};
        for (ListNode *node:lists) {
            while (node) {
                arr.push_back(node->val);
                node = node->next;
            }
        }
        
        // sorted
        sort(arr.begin(),arr.end());
        
        // recover linked-list
        ListNode *root = new ListNode(0);
        ListNode *temp = root;
        for (int val:arr) {
            temp->next = new ListNode(val);
            temp = temp-> next;
        }
        return root->next;
    }
};