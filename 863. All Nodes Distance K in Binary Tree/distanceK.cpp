/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    // global parameter
    map<TreeNode*,TreeNode*> node_link;
    set<TreeNode*> node_visited;
    vector<int> output;
    vector<int> distanceK(TreeNode* root, TreeNode* target, int k) {
        // How to go back? use graph
        find_parent(root); //create graph: node_link
        dfs(target, k);
        return output;
    }

    // Tree to Graph
    void find_parent(TreeNode* node) {
        if (!node) { return; }
        if (node->left) { node_link[node->left] = node; }
        if (node->right) { node_link[node->right] = node; }
        find_parent(node->left);
        find_parent(node->right);
    }

    // Scan All Graph
    void dfs(TreeNode* node, int d) {
        // visited -> continue
        if (node_visited.count(node)!=0) { return; }
        else { node_visited.insert(node); }
        // step >= k
        if (d==0) { output.push_back(node->val); }
        else if (d<0) { return; }
        // step < k
        // goto L
        if (node->left) { dfs(node->left, d-1); }
        // goto R
        if (node->right) { dfs(node->right, d-1); }
        // go back
        if (node_link.find(node)!=node_link.end()) { dfs(node_link[node], d-1); }
    }
};