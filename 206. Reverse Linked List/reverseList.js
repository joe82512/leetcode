/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var reverseList = function(head) {
    var r = null
    while (head != null) {
        temp = head.next
        head.next = r
        r = head
        head = temp
        // [head.next, r, head] = [r, head, head.next]
    }
    return r
};

// Runtime 94 ms / Memory 44.1 MB
// debug: https://jsfiddle.net/