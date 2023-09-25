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
    vector<vector<int>> levelOrder(TreeNode* root) {
        vector<vector<int>> output;
        // empty
        if (root == NULL) { return output; }
        // BFS
        queue<TreeNode*> nodeList;
        nodeList.push(root);

        while (!nodeList.empty()) {
            // same depth            
            int n = nodeList.size();
            vector<int> valueList;
            for(int i=0; i<n; i++){
                // popup(0)
                TreeNode* node = nodeList.front();
                nodeList.pop();
                valueList.push_back(node->val);
                // push_back
                if(node->left != NULL) { nodeList.push(node->left); }
                if(node->right != NULL) { nodeList.push(node->right); }
            }
            // next depth
            output.push_back(valueList);
        }

        return output;
    }
};