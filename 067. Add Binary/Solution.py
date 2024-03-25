class Solution(object):
    # Runtime 20 ms / Memory 11.9 MB
    def addBinary_1(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        def fullAdder(A,B,c_in):
            Sum = (A^B)^c_in #sum
            c_out = (A&B)|(B&c_in)|(A&c_in) #carry
            return (Sum,c_out)
        
        max_len = max(len(a),len(b))
        a = (max_len-len(a))*"0" + a
        b = (max_len-len(b))*"0" + b
        (Sum,c_out) = (0,0)
        string = ""
        # ripple adder
        for i in range(max_len-1,-1,-1):
            Sum, c_out = fullAdder(int(a[i]),int(b[i]),c_out)
            string = str(Sum) + string 
        if (c_out):
            return str(c_out) + string
        else:
            return string
        
    # Runtime 14 ms / Memory 11.7 MB
    def addBinary_2(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        num_a = int(a,2)
        num_b = int(b,2)
        str_bin = bin((num_a + num_b))[2:] #"0b****"
        return str_bin