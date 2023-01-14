# -*- coding: utf-8 -*-
from collections import defaultdict
class Solution(object):
    # Runtime 1885 ms / Memory 115.6 MB
    def validPath_1(self, n, edges, source, destination):
        path = defaultdict(list)        
        for e in edges:
            path[e[0]].append(e[1])
            path[e[1]].append(e[0])

        queue = [source]
        visited = [False]*n
        while queue:
            curr = queue.pop(0)
            if curr == destination:
                return True
            elif curr in path and not visited[curr]:
                queue += path[curr]
            visited[curr] = True
        return False

    # Runtime 1663 ms / Memory 110.3 MB
    def validPath_2(self, n, edges, source, destination):
        disjoinSet = DisjoinSet(n)
        for edge in edges:
            disjoinSet.connect(edge[0],edge[1])
        return disjoinSet.find(source) == disjoinSet.find(destination)



class DisjoinSet():
    def __init__(self,iSize):
        self.parent = [i for i in range(iSize)] #root(min) list
    
    def find(self,x): #find root index
        root = self.parent[x]
        while self.parent[root] != root:
            root = self.parent[root]
        return root

    def connect(self,left,right): #update parent
        (leftRoot, rightRoot) = (self.find(left), self.find(right))
        if leftRoot < rightRoot:
            self.parent[rightRoot] = leftRoot
        else:
            self.parent[leftRoot] = rightRoot