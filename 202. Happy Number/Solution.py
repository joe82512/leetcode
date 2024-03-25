class Solution(object):
    # Runtime 19 ms / Memory 11.7 MB
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        def algo(num):
            temp = 0
            while (num>0):
                t = num%10
                num = num//10
                temp += t*t
            return temp
        
        # Loop Cycle
        s1 = s2 = n
        while(True):
            s1 = algo(s1)
            s2 = algo(algo(s2))
            if (s1==1 or s2==1):
                return True
            if (s1 == s2):
                break
        return (s1==1)
    
    # Runtime 14 ms / Memory 11.9 MB
    def isHappy_2(self, n):
        """
        :type n: int
        :rtype: bool
        """
        visit = set()
        while (n!=1):
            temp = 0
            while (n):
                t = n%10
                n = n//10
                temp += t*t

            n = temp
            if n in visit: #loop number
                return False
            else:
                visit.add(n)
        return True
    
    # Runtime 12 ms / Memory 11.5 MB
    def isHappy_3(self, n):
        """
        :type n: int
        :rtype: bool
        """
        while (True):
            temp = 0
            while (n):
                t = n%10
                n = n//10
                temp += t*t
            
            n = temp
            if (n==1):
                return True
            elif (n==7): #limit to 1
                return True
            elif (n//10==0):
                break
        return (n==1)