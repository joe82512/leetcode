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
    TreeNode* mergeTrees(TreeNode* root1, TreeNode* root2) {
        if (!root1) { return root2; } //maybe root2==NULL
        else if (!root2) { return root1; }
        // else
        TreeNode* output = new TreeNode();
        output->val = root1->val + root2->val;
        output->left = mergeTrees(root1->left,root2->left);
        output->right = mergeTrees(root1->right,root2->right);
        return output;
    }
};