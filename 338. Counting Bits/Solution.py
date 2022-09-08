# -*- coding: utf-8 -*-
class Solution:
    # Runtime 409 ms / Memory 17.1 MB
    def countBits_1(self, n):
        # binary
        result = []
        for i in range(n+1):
            r = 0
            while i>0:
                r = r + i%2
                i = i//2
            result.append(r)
            # result.append(bin(i).count('1'))        
        return result

    # Runtime 227 ms / Memory 14.7 MB
    def countBits_2(self, n):
        # [0,1,1,2,1,2,2,3,1,2,2,3,2,3,3,4,1,...etc]
        result = [0]
        for i in range(1,n+1):
            result.append(result[i//2] + i%2)
        return result



if __name__ == '__main__':
    print(Solution().countBits_1(2))
    print(Solution().countBits_1(5))
    print("=====================================")
    print(Solution().countBits_2(2))
    print(Solution().countBits_2(5))