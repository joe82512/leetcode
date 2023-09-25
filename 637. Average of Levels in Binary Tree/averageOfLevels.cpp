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
    vector<double> averageOfLevels(TreeNode* root) {
        vector<double> output;
        queue<TreeNode*> q;
        q.push(root);
        // BFS
        while (!q.empty()) {
            double temp = 0;
            int n = q.size();
            // same depth
            for (int i=0; i<n; i++) {
                TreeNode* node = q.front();
                q.pop();
                temp += node->val;
                if (node->left) { q.push(node->left); }
                if (node->right) { q.push(node->right); }
            }
            temp = temp/n;
            output.push_back(temp);
        }
        return output;
    }
};