class Solution(object):
    # Runtime 494 ms / Memory 12.8 MB
    def coinChange_1(self, coins, amount): #BFS
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if (amount==0):
            return 0

        queue = [(amount,0)] #(residue, num_coin)
        visited = set() #same combine , Time Limit if not
        coins.sort() #for early stop

        while queue:
            #print(queue)
            (residue, num_coin) = queue.pop(0)
 
            for coin in coins:
                temp_residue = residue - coin
 
                if (temp_residue==0):
                    return num_coin+1
                elif (temp_residue in visited):
                    continue
                elif (temp_residue<0): #early stop
                    break
                else:
                    queue.append((temp_residue,num_coin+1))
                    visited.add(temp_residue)
 
        return -1
    
    # Runtime 754 ms / Memory 12.1 MB
    def coinChange_2(self, coins, amount): #DP
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        ### dp[idx]=min(cnt), idx=sum of coin
        dp = [float('inf')] * (amount+1)
        dp[0] = 0

        coins.sort()
        for i in range(1, amount + 1): #sum of coin
            for coin in coins:
                if coin <= i:
                    dp[i] = min(dp[i], dp[i - coin] + 1) #get min count
                else:
                    break #early break
        
        # print(dp)
        if dp[-1] == float('inf'): #no combine
            return -1
        else:
            return dp[-1]
        
    # Runtime 31 ms / Memory 11.6 MB
    def coinChange_3(self, coins, amount): #bit operation
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        
        cnt = 0
        seen = 1 << amount # 100...0
        
        while (seen & 1) != 1: # last bit != 1
            cur = seen
            for coin in coins:
                cur = (seen >> coin) | cur
            # print("seen: ",bin(seen))
            # print("cur : ",bin(cur))
            # print("===============================")
            if cur == seen: #no combine
                return -1
            else:
                seen = cur
                cnt += 1

        return cnt
    
    """
    ex: [1,2,5], 11
    ans: 3
    ('seen: ', '0b100000000000')
    ('cur : ', '0b111001000000')
    ===============================
    ('seen: ', '0b111001000000')
    ('cur : ', '0b111111110010')
    ===============================
    ('seen: ', '0b111111110010')
    ('cur : ', '0b111111111111') => full combine
    ===============================

    ex: [2,5], 11
    ans: 4
    ('seen: ', '0b100000000000')
    ('cur : ', '0b101001000000')
    ===============================
    ('seen: ', '0b101001000000')
    ('cur : ', '0b101011010010')
    ===============================
    ('seen: ', '0b101011010010')
    ('cur : ', '0b101011110110')
    ===============================
    ('seen: ', '0b101011110110')
    ('cur : ', '0b101011111111') => 1,3 not combine
    ===============================
    """