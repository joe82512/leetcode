# -*- coding: utf-8 -*-

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    # Runtime 27 ms / Memory 13.8 MB
    def distanceK_1(self, root, target, k):
        def find_parent(node): #Tree to Graph
            if not node:
                return
            
            if node.left:
                parent[node.left] = node
            if node.right:
                parent[node.right] = node
                
            find_parent(node.left)
            find_parent(node.right)
            
            
        def dfs(node, k): #Scan All Graph
            if node not in visited:
                visited.add(node)
            else:
                return
            
            if k == 0:
                res.append(node.val)
                
            if node.left:
                dfs(node.left, k-1)
            if node.right:
                dfs(node.right, k-1)
                
            if node in parent:
                dfs(parent[node], k-1)

        visited, res, parent = set(), [], {}
        find_parent(root)
        dfs(target, k)
        
        return res


    # Runtime 20 ms / Memory 13.8 MB
    def distanceK_2(self, root, target, k):
        visited, res, parent = {}, [], {}

        #Tree to Graph
        queue = [root]
        while (queue):
            L = len(queue)
            for i in range(L):
                node = queue.pop(0)
                if node.left:
                    parent[node.left] = node
                    queue.append(node.left)
                if node.right:
                    parent[node.right] = node
                    queue.append(node.right)
        
        #Scan All Graph
        queue = [target]
        while (queue) and (k>0):
            L = len(queue)
            for i in range(L):
                node = queue.pop(0)
                visited[node.val] = 1
                if (node.left) and (node.left.val not in visited):
                    queue.append(node.left)
                if (node.right) and (node.right.val not in visited):
                    queue.append(node.right)
                if (node in parent) and (parent[node].val not in visited):
                    queue.append(parent[node])
            k = k-1

        while (queue):
            node = queue.pop(0)
            res.append(node.val)

        return res