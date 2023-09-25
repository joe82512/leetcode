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
    vector<TreeNode*> findDuplicateSubtrees(TreeNode* root) {
        unordered_map<string, int> cnt;
        vector<TreeNode*> output;
        DFS(root, cnt, output);
        return output;
    }

    string DFS(TreeNode* node, unordered_map<string, int> &cnt, vector<TreeNode*> &output) {
        if (!node) { return "X"; }
        // else
        string key = to_string(node->val) + "," + DFS(node->left, cnt, output) + "," + DFS(node->right, cnt, output);
        // check same str(node values)
        cnt[key]++;
        if (cnt[key]==2) { output.push_back(node); }

        return key;
    }
};