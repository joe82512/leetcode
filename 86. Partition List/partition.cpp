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
    ListNode* partition(ListNode* head, int x) {
        ListNode* leftList = new ListNode(0);
        ListNode* goLeft = leftList;
        ListNode* rightList = new ListNode(0);
        ListNode* goRight = rightList;

        while (head) {
            if (head->val < x) {
                goLeft->next = head;
                goLeft = goLeft->next;
            }
            else {
                goRight->next = head;
                goRight = goRight->next;
            }
            head = head->next;
        }
        
        goLeft->next = rightList->next; //combine, ignore dummy (rightList) head
        goRight->next = nullptr; //tail
        return leftList->next; //ignore dummy head
    }
};