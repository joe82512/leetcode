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
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode* root = new ListNode(0);
        ListNode* ls = root;
        int val = 0;
        while (l1 or l2 or val) {
            if (l1) {
                val += l1->val;
                l1 = l1->next;
            };
            if (l2) {
                val += l2->val;
                l2 = l2->next;
            };
            ListNode* nextNode = new ListNode(val%10);
            ls->next = nextNode;
            ls = ls->next;
            val = val/10;
        };
        return root->next;
    }
};