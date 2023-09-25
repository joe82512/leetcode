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
    ListNode* middleNode(ListNode* head) {
        // fast and slow pointer
        ListNode* slow = head; // 1 step
        ListNode* fast = head; // 2 step
        while (fast and fast->next) {
            slow = slow->next;
            fast = fast->next->next;
        }
        return slow;
    }
};