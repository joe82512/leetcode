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
    int sumOfLeftLeaves(TreeNode* root) {
        int output = 0;
        DFS(root, 0, output);
        return output;
    }

    void DFS(TreeNode *node, bool isLeft, int &output) {
        // goto end
        if (!node) { return; }
        // goto last
        if ( isLeft && !node->left &&  !node->right ) {
            output += node->val;
        }
        // next step
        DFS(node->left, 1, output);
        DFS(node->right, 0, output);
    }
};