/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    int deepestLeavesSum(TreeNode* root) {
        int r = 0;
        queue<TreeNode*> q;
        // BFS
        q.push(root);
        while (!q.empty()) {
            int depth_total = 0;
            int n = q.size();
            for (int i=0; i<n; i++) {
                // sum of same depth
                TreeNode *node = q.front();
                q.pop();
                depth_total += node->val;
                // add L
                if (node->left) { q.push(node->left); }
                // add R
                if (node->right) { q.push(node->right); }
            }
            // update total
            r = depth_total;
        }
        return r;
    }
};