# -*- coding: utf-8 -*-
class Solution(object):
    # Runtime 24 ms / Memory 13.7 MB
    def detectCapitalUse_1(self, word):
        w1 = word.upper()
        w2 = word.lower()
        w3 = word.capitalize()
        compare = [w1, w2, w3]
        return (word in compare)

    # Runtime 19 ms / Memory 13.6 MB
    def detectCapitalUse_2(self, word):
        cnt = 0
        for w in word:
            if w.isupper():
                cnt += 1
        
        if word[0].isupper():
            if cnt==len(word) or cnt==1 :
                return True 
        else:
            if cnt==0:
                return True

        return False