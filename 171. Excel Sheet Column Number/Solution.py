# -*- coding: utf-8 -*-
class Solution(object):
    # Runtime 11 ms / Memory 13.6 MB
    def titleToNumber_1(self, columnTitle):
        r = 0
        for word in columnTitle:
            r = r*26 + (ord(word)-64) #A=65
        return r

    # Runtime 19 ms / Memory 13.4 MB
    def titleToNumber_2(self, columnTitle):
        alphabet = {chr(i+64):i for i in range(1,27)}
        r = 0
        for word in columnTitle:
            r = r*26 + alphabet[word]
        return r