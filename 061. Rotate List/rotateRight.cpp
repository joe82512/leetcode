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
    ListNode* rotateRight(ListNode* head, int k) {
        // empty data
        if (!head) { return head; }
        else if (!head->next) { return head; }
        // calculate step
        int cnt = 1;
        ListNode *a = head;
        while (a->next) {
            cnt++;
            a = a->next;
        }
        int step = k%cnt;

        // return
        if (step==0) { return head; }
        // else
        //[a(n),b(l-n)],a(n),b(l-n) = a(n),[b(l-n),a(n)],b(l-n)
        a->next = head;
        for (int i=0; i<(cnt-step); i++) { a = a->next; }
        ListNode *b = a->next;
        a->next = NULL;
        return b;
        /*
        #  [5], 1 , 2 , 3 , 4 ,[5], 1 , 2 , 3 , 4 ,... => a.next = head
        #a: 5 , 1 , 2 ,[a], 4 , 5 , 1 , 2 ,[a], 4 ,... => Loop: a.next
        #b: 5 , 1 , 2 ,[a],[b], 5 , 1 , 2 ,[a],[b],... => b = a.next
        #a:                [b], 5 , 1 , 2 ,[a]         => a.next = None
        */
    }
};