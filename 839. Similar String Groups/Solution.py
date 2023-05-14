# -*- coding: utf-8 -*-
class Solution(object):
    # Runtime 2311 ms / Memory 13.8 MB
    def numSimilarGroups_1(self, strs):
        r = 0
        n = len(strs)
        visit = [0]*n
        queue = []
 
        for v in range(n):
            if (visit[v]): #v as i, if similar 1
                continue
            #else
            visit[v] = 1
            r += 1
 
            queue.append(strs[v])
            while (queue):
                s = queue.pop(0) #BFS or DFS
                for i in range(n):
                    if (visit[i]):
                        continue
                    elif (len(s) != len(strs[i])):
                        continue
                    #else
                    # compare string
                    different = 0
                    for j in range(len(strs[i])):
                        if (s[j]!=strs[i][j]):
                            different += 1
                    # differnt result
                    if (different==0 or different==2):
                        visit[i] = 1 #v as i, if similar 1
                        queue.append(strs[i])
                        
        return r

    # Runtime 284 ms / Memory 15.6 MB
    def numSimilarGroups_2(self, strs):
        def is_similar(s1, s2):
            diff_count = 0
            for i in range(len(s1)):
                if s1[i] != s2[i]:
                    diff_count += 1
                if diff_count > 2:
                    return False
            return True

        def dfs(index, visited):
            if visited[index]:
                return 0
            visited[index] = True
            for i in range(len(strs)):
                if not visited[i] and is_similar(strs[index], strs[i]):
                    dfs(i, visited)
            return 1

        visited = [False] * len(strs)
        groups = 0
        for i in range(len(strs)):
            groups += dfs(i, visited)

        return groups