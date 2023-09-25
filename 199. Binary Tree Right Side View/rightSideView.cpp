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
    vector<int> rightSideView(TreeNode* root) {
        vector<int> res;
        dfs(root,0,res);
        return res;
    }

    void dfs(TreeNode* node, int depth, vector<int>& res) {
        // goto end
        if (!node) { return; }
        // else
        if (res.size()==depth) { res.push_back(node->val); } //1: get middle number
        dfs(node->right, depth+1, res); //2: goto next step, right must priority
        dfs(node->left, depth+1, res);

    }
};