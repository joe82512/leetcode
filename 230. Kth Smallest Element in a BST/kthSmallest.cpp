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
    int kthSmallest(TreeNode* root, int k) {
        // BST -> DFS must sort
        vector<int> sort_val;
        dfs(root, sort_val);
        return sort_val[k-1];
    }
    
    void dfs (TreeNode* node, vector<int>& sort_val) {
        if (!node) { return; }
        dfs(node->left, sort_val); //L
        sort_val.push_back(node->val); //mid
        dfs(node->right, sort_val); //R
    }
};