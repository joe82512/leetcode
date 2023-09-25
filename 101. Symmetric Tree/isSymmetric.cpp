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
    bool isSymmetric(TreeNode* root) {
        return check(root->left,root->right);
    }

    bool check(TreeNode* p, TreeNode* q) {
        // goto leaf
        if (!p && !q) { return true; }
        else if (!p || !q) { return false; }
        // check
        if (p->val != q->val) { return false; }
        else {
            bool L = check(p->left,q->right); //mirror
            bool R = check(p->right,q->left); //mirror
            return L && R;
        }
    }
};