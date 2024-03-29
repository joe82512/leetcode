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
 * @return {number}
 */
var maxDepth = function(root) {
    if (root) {
        return Math.max(maxDepth(root.left), maxDepth(root.right))+1
    }
    else {
        return 0
    }    
};

// Runtime 76 ms / Memory 44.7 MB
// debug: https://jsfiddle.net/