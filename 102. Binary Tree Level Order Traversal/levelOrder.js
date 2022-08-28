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
 * @return {number[][]}
 */
var levelOrder = function(root) {
    var queue = [root]
    var result = []
    
    while (queue.length > 0) {
        let level = []
        let q_len = queue.length
        for (i=0;i<q_len;i++) {
            let node = queue.shift()
            if (node) {
                level.push(node.val)
                if (node.left) {
                    queue.push(node.left)
                }
                if (node.right){
                    queue.push(node.right)
                }                
            }
        }
        
        if (level) {
            result.push(level)
        }
    }
    if (root) {
        return result
    }
    else {
        return []
    }
};

// Runtime 80 ms / Memory 44.5 MB
// debug: https://jsfiddle.net/