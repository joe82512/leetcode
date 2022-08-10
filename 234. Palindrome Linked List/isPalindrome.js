/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {boolean}
 */
var isPalindrome = function(head) {
    var r_list = []
    while (head != null) {
        r_list.push(head.val)
        head = head.next
    }
    re_list = [...r_list].reverse()
    for (let i = 0; i < r_list.length; i++) {
        if (r_list[i] !== re_list[i]) {
            return  false
        }
    }
    return true
};

// Runtime 234 ms / Memory 88 MB
// debug: https://jsfiddle.net/