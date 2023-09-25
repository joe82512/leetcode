/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Codec {
public:

    // Encodes a tree to a single string.
    string serialize(TreeNode* root) {
        ostringstream tree2str;
        DFS(root, tree2str);
        return tree2str.str();
    }

    void DFS(TreeNode* node, ostringstream& tree2str) {
        if (!node) { tree2str << "X" << " "; return; }
        //else
        tree2str << to_string(node->val) << " ";
        DFS(node->left, tree2str);
        DFS(node->right, tree2str);
    }

    // Decodes your encoded data to tree.
    TreeNode* deserialize(string data) {
        istringstream str2tree(data);
        TreeNode *tree = BinTree(str2tree);
        return tree;
    }

    TreeNode* BinTree(istringstream& str2tree) {
        string val;
        str2tree >> val;
        if (val == "X") { return nullptr; }
        //else
        TreeNode* node = new TreeNode(stoi(val));
        node->left = BinTree(str2tree);
        node->right = BinTree(str2tree);
        return node;
    }
};

// Your Codec object will be instantiated and called as such:
// Codec ser, deser;
// TreeNode* ans = deser.deserialize(ser.serialize(root));