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
    int maxDepth(TreeNode* root) {
        // empty
        if (root == NULL) { return 0; }
        // BFS
        int depth = 0;
        queue<TreeNode*> nodeList;
        nodeList.push(root);

        while (!nodeList.empty()) {
            // same depth
            int n = nodeList.size();
            for(int i=0; i<n; i++){
                // popup(0)
                TreeNode* node = nodeList.front();
                nodeList.pop();
                // push_back
                if(node->left != NULL) { nodeList.push(node->left); }
                if(node->right != NULL) { nodeList.push(node->right); }
            }
            // next depth
            depth++;
        }
        return depth;
    }
};