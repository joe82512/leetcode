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
    bool isPalindrome(ListNode* head) {
        // create list
        vector<int> values;
        ListNode *node = head;
        while (node) {
            values.push_back(node->val);
            node = node->next;
        }
        // check palindrome
        vector<int> sortValues = values;
        reverse(sortValues.begin(),sortValues.end());
        return (sortValues==values);
    }
};