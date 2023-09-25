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
    vector<vector<int>> pathSum(TreeNode* root, int targetSum) {
        vector<int> path;
        vector<vector<int>> res;
        dfs (root, targetSum, path, res);
        return res;
    }

    void dfs (TreeNode* node, int target, vector<int> &path, vector<vector<int>>& res) {
        if (!node) { return; }
        path.push_back(node->val);
        if (!node->left and !node->right and target==node->val) {
            res.push_back(path);
            // return; //reference
        }
        dfs(node->left, target-node->val, path, res);
        dfs(node->right, target-node->val, path, res);
        path.pop_back();
    }
};



class Solution {
public:
    vector<vector<int>> pathSum(TreeNode* root, int targetSum) {
        vector<int> path;
        vector<vector<int>> res;
        dfs (root, targetSum, path, res);
        return res;
    }

    void dfs (TreeNode* node, int target, vector<int> path, vector<vector<int>>& res) {
        if (!node) { return; }
        path.push_back(node->val);
        if (!node->left and !node->right and target==node->val) {
            res.push_back(path);
            return; //slower
        }
        dfs(node->left, target-node->val, path, res);
        dfs(node->right, target-node->val, path, res);
        path.pop_back();
    }
};