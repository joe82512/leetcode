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
    int maxDepth(Node* root) {
        if (!root) { return 0; } //case []
        int depth = 0;
        queue<Node*> q;
        q.push(root);
        // BFS
        while (!q.empty()) {
            depth += 1;
            // same level
            int n = q.size();
            for (int i=0; i<n; i++) {
                Node* node = q.front();
                q.pop();
                for (auto child:node->children) { q.push(child); }
            }
        }
        return depth;
    }
};