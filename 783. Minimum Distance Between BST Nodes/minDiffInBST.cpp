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
    int prev = -1;
    int r = 1E5;
    int minDiffInBST(TreeNode* root) {
        getNode(root);
        return r;
    }
    void getNode(TreeNode* node) {
        if (node) {
            getNode(node->left);
            if (prev != -1) {
                r = min(r, node->val - prev);
            }
            prev = node->val;
            getNode(node->right);
        }
        else {
            return;
        }
    }
};