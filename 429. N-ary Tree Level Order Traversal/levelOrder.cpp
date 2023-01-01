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
    // void dfs (Node* node, int path, map<int, vector<int>>& output) {
    void dfs (Node* node, int path, vector<vector<int>>& output) {
        if (!node) {
            return;
        }

        /*
        // map method
        if (output.find(path) == output.end()) {
            vector<int> tmp = {node->val};
            output[path] = tmp;
        }
        else {
            output[path].push_back(node->val);
        }
        */

        // vector method
        if (output.size() <= path) {
            output.resize(output.size()+1);
        }
        output[path].push_back(node->val);
        
        for (auto nodes:node->children) {
            dfs(nodes, path+1, output);
        }
    }
    vector<vector<int>> levelOrder(Node* root) {
        /*
        // map method
        map<int, vector<int>> output; //not unordered_map
        dfs(root, 0, output);
        vector<vector<int>> res;
        for (auto o:output) {
            res.push_back(o.second);
        }
        return res;
        */
        vector<vector<int>> output;
        dfs(root, 0, output);
        return output;
    }
};