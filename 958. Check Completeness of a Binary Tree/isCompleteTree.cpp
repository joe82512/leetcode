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
    bool isCompleteTree(TreeNode* root) {
        queue<TreeNode*> q;
        bool null_flag = false;
        // BFS
        q.push(root);
        while (!q.empty()) {
            TreeNode* node = q.front();
            q.pop();
            // first null
            if (!node) { null_flag = true; }
            // if fisrt null not last null
            else if (node && null_flag) { return false; }
            // goto next node
            else {
                q.push(node->left);
                q.push(node->right);
            }
        }
        return true;
    }
};