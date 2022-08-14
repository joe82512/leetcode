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
var isValidBST = function(root) {
    var traverse = (root,low,high) => {
        if (!root) {
            return true
        }
        else if (low >= root.val) { //can't use !(low < root.val <high)
            return false
        }
        else if (high <= root.val) {
            return false
        }
        else {
            return traverse(root.left,low,root.val) && traverse(root.right,root.val,high)
        }
    }
    return traverse(root,low=-Infinity,high=Infinity)
};

// Runtime 78 ms / Memory 46.5 MB
// debug: https://jsfiddle.net/