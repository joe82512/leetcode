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
    bool isValidBST(TreeNode* root) {
        long long int boundaryCondition_L = LLONG_MIN; //less than min spec
        long long int boundaryCondition_R = LLONG_MAX; //large than max spec
        return DFS(root, boundaryCondition_L, boundaryCondition_R);
    }

    bool DFS(TreeNode* node, long long int BC_L, long long int BC_R) {
        if (!node) { return true; }
        else if (node->val <= BC_L ) { return false; }
        else if (node->val >= BC_R ) { return false; }
        else {
            bool L = DFS(node->left, BC_L, node->val);
            bool R = DFS(node->right, node->val, BC_R);
            return (L && R);
        }
    }
};