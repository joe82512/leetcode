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
    int minDiffInBST(TreeNode* root) {
        // if (!root) { return 0; }
        // else if (!root->left && !root->right) { return root->val; }
        // note : node >= 2 , impossible case
        int output = INT_MAX;
        int temp = -1;
        DFS(root, temp, output);
        return output;
    }
    
    void DFS(TreeNode* node,int &temp, int &output) {
        if (!node) { return; }
        // else
        DFS(node->left,temp,output);
        // First node case
        if (temp != -1) {
            output = min(output, node->val-temp); //val > temp
        }
        temp = node->val;
        DFS(node->right,temp,output);
    }
};