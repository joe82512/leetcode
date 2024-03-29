/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} p
 * @param {TreeNode} q
 * @return {boolean}
 */
var isSameTree = function(p, q) {
    if (p && q) {
        if (p.val != q.val) {
            return false
        }
        else {
            return isSameTree(p.left,q.left) && isSameTree(p.right,q.right)
        }
    }
    else {
        return p===q
    }
};

// Runtime 88 ms / Memory 42.2 MB
// debug: https://jsfiddle.net/