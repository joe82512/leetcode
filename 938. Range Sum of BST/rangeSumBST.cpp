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
    int rangeSumBST(TreeNode* root, int low, int high) {
        // create sort vector by DFS
        vector<int> values;
        DFS(root, values);
        // accumulator if match
        int sum = 0;
        for (auto v:values) {
            if ( high>=v && v>=low ) { sum += v; }
        }
        return sum;
    }

    void DFS(TreeNode* node, vector<int> &values) {
        // goto END
        if (!node) { return; }
        // else
        DFS(node->left,values); //L
        values.push_back(node->val); //middle
        DFS(node->right,values); //R
    }
};