class Solution(object):
    # Runtime 11 ms / Memory 11.6 MB
    def wordBreak_1(self, s, wordDict): #BFS
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        queue = [s] #(residue_string)
        visited = set() #same combine
        # if visited use array: 23mS , set: 6mS
 
        while queue:
            #print(queue)
            (residue) = queue.pop(0)
 
            for word in wordDict:
                if (residue[0:len(word)]==word):
                    right_s = residue[len(word):]
 
                    if (right_s==""):
                        return True
                    elif (right_s not in visited):
                        queue.append(right_s)
                        visited.add(right_s)
 
        return False
    
    # Runtime 21 ms / Memory 11.8 MB
    def wordBreak_2(self, s, wordDict): #DP
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        ### dp[idx]=combine pass/fail, idx=string index
        dp = [False] * (len(s)+1)
        dp[0] = True
        
        for i in range(1, len(s)+1): #string index
            for j in range(i): #s[0:j], s[j:i] both pass 
                if (dp[j]) and (s[j:i] in wordDict):
                    dp[i] = True
                    break
        
        # print(dp)
        return dp[-1]