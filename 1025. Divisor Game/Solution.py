# -*- coding: utf-8 -*-
class Solution:
    # Runtime 30 ms / Memory 13.5 MB
    def divisorGame_1(self, n):
        '''
        grab even number
        just always choose 1
        if n odd
            A : odd -> even
            B : even -> odd
            loop ---> B get 2
        '''        
        return (n%2 == 0)

    # Runtime ms / Memory MB
    def divisorGame_2(self, n):
        pass



if __name__ == '__main__':
    print(Solution().divisorGame_1(2))
    print(Solution().divisorGame_1(3))
    print("=====================================")