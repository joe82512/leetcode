from math import factorial as fc

class Solution(object):
    # Runtime 35 ms / Memory 13.3 MB
    def numTrees_1(self, n):
        '''
        f(0)=1; f(1)=1; f(2)=2;
        f(n) = f(0) * f(n-1) + f(1) * f(n-2) + … + f(n-1) * f(0)
        '''        
        fn_list = [0 for i in range(n+2)]
        fn_list[0],fn_list[1] = 1,1
        for j in range(2,n+1):
            for k in range(1,j+1):
                fn_list[j] += fn_list[k-1] * fn_list[j-k]
        return fn_list[-1]

    # Runtime 29 ms / Memory 13.6 MB
    def numTrees_2(self, n):
        '''
        Catalan Numbers
        f[n] = (2n)!/(n! * n! * (n+1))
        '''
        return fc(2*n)//fc(n)//fc(n)//(n+1)