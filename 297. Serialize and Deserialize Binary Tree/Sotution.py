# -*- coding: utf-8 -*-

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:
    # Runtime 155 ms / Memory 23.5 MB
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        tree2list =[]
        def DFS(root):
            if not root:
                tree2list.append("X")
            if root:
                tree2list.append(str(root.val))
                DFS(root.left)
                DFS(root.right)
        DFS(root)
        return ','.join(tree2list)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        list2tree = data.split(",")
        def BinTree():
            if list2tree:
                value = list2tree.pop(0)
                if(value == "X"):
                    return None
                else:
                    node = TreeNode(int(value))
                    node.left= BinTree()
                    node.right = BinTree()
                return node
        
        root = BinTree()
        
        return root

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))