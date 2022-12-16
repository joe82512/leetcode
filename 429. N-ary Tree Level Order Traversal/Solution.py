# -*- coding: utf-8 -*-
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution(object):
    # Runtime 67 ms / Memory 16.3 MB
    def levelOrder_1(self, root):
        if not root:
            return []
        result, queue = [], [root]
        while len(queue) != 0:
            res = []
            for i in range(len(queue)):
                n = queue.pop(0)
                res.append(n.val)
                queue += n.children
            result.append(res)
        return result

    # Runtime 43 ms / Memory 16.5 MB
    def levelOrder_2(self, root):
        output = {}
        self.getLevel(root,0,output)
        return output.values()

    def getLevel(self,node,path,output):
        if not node:
            return
        if path not in output:
            output[path] = [node.val]
        else:
            output[path] += [node.val]
        for nodes in node.children:
            self.getLevel(nodes,path+1,output)