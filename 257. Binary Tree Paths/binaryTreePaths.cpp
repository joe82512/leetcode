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
    vector<string> binaryTreePaths(TreeNode* root) {
        // DFS or BFS
        vector<string> output;
        DFS(root, "", output);
        return output;
    }

    void DFS(TreeNode *node, string s, vector<string>& output) {
        // goto end
        if (!node) { return; }
        // else
        s = s + to_string(node->val); //mid
        if (!node->left && !node->right) { output.push_back(s); } //mid as end
        DFS(node->left, s+"->", output); //L
        DFS(node->right, s+"->", output); //R
    }
};