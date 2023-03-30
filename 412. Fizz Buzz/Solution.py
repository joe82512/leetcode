# -*- coding: utf-8 -*-
class Solution(object):
    # Runtime 26 ms / Memory 14.2 MB
    def fizzBuzz_1(self, n):
        r = []
        for i in range(1,n+1):
            a = ""
            if (i%3==0):
                a += "Fizz"
            if (i%5==0):
                a += "Buzz"
            if (a==""):
                a += str(i)
            r.append(a)
        return r

    # Runtime 25 ms / Memory 14.2 MB
    def fizzBuzz_2(self, n):
        r = []
        for i in range(1,n+1):
            if (i%3==0) and (i%5==0):
                r.append("FizzBuzz")
            elif (i%3==0):
                r.append("Fizz")
            elif (i%5==0):
                r.append("Buzz")
            else:
                r.append(str(i))
        return r