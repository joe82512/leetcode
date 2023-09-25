/*
// Definition for a Node.
class Node {
public:
    int val;
    vector<Node*> children;

    Node() {}

    Node(int _val) {
        val = _val;
    }

    Node(int _val, vector<Node*> _children) {
        val = _val;
        children = _children;
    }
};
*/

class Solution {
public:
    vector<vector<int>> levelOrder(Node* root) {
        // empty
        vector<vector<int>> output;
        if (!root) { return {}; }
        // BFS
        queue<Node*> q;
        q.push(root);
        while (!q.empty()) {
            vector<int> temp;
            int n = q.size();
            for (int i=0; i<n; i++) {
                Node* node = q.front();
                q.pop();
                temp.push_back(node->val);
                // append all child
                for (auto child: node->children) { q.push(child); }
            }
            output.push_back(temp);
        }

        return output;
    }
};