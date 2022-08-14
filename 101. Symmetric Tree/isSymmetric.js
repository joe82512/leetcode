/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {boolean}
 */

var isSymmetric = function(root) {
    var isSym = (L,R) => {
        if (L && R && L.val===R.val) {
            return isSym(L.left,R.right) && isSym(L.right,R.left)
        }
        else {
            return L===R
        }
    }
    
    if (root) {
        return isSym(root.left,root.right)
    }
    else {
        return true
    }
};

// Runtime 128 ms / Memory 44.1 MB
// debug: https://jsfiddle.net/