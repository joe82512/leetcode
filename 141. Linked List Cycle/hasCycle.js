/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */

/**
 * @param {ListNode} head
 * @return {boolean}
 */
var hasCycle = function(head) {
    a = head
    b = head
    while (b && b.next) {
        a = a.next
        b = b.next.next
        if (a == b) {
            return true
        }
    }
    return false
};

// Runtime 140 ms / Memory 44.3 MB
// debug: https://jsfiddle.net/