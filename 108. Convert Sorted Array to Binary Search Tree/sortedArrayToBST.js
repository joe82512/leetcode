/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {number[]} nums
 * @return {TreeNode}
 */
var sortedArrayToBST = function(nums) {
    if (!nums == null || !nums.length) {
        return null
    }
    else {
        let p = Math.floor(nums.length/2) //must define
        const n = new TreeNode(nums[p]) //must define
        n.left = sortedArrayToBST(nums.slice(0,p))
        n.right = sortedArrayToBST(nums.slice(p+1,nums.length))
        return n
    }
};

// Runtime 84 ms / Memory 44.4 MB
// debug: https://jsfiddle.net/