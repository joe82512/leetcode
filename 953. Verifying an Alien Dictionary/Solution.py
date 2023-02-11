# -*- coding: utf-8 -*-
class Solution(object):
    # Runtime 23 ms / Memory 13.6 MB
    def isAlienSorted_1(self, words, order):
        alien_map = {key: idx for idx,key in enumerate(order)}

        for i in range(1,len(words)):
            word1, word2 = words[i-1], words[i]
            n = min(len(word1), len(word2))
            for k in range(n):
                if word1[k] != word2[k]:
                    if alien_map[word1[k]] > alien_map[word2[k]]:
                        return False #string not sort
                    else:
                        break #next char
            
            if (len(word1) > len(word2)) & (word1[0:len(word2)] == word2):
                return False #word not sort
        return True

    # Runtime 30 ms / Memory 13.6 MB
    def isAlienSorted_2(self, words, order):
        alien_map = {key: idx for idx,key in enumerate(order)}

        decode = []
        for word in words:
            phrase = [alien_map[w] for w in word]
            decode.append(phrase)

        return sorted(decode) == decode