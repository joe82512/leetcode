# -*- coding: utf-8 -*-
class Solution:
    # Runtime 95 ms / Memory 13.5 MB
    def canConstruct_1(self, ransomNote, magazine):
        if (len(ransomNote)>len(magazine)):
            return False
        
        #else : two pointer
        ransomNote = sorted(ransomNote)
        magazine = sorted(magazine)
        i = j = 0
        while i<len(ransomNote) and j<len(magazine):
            if (ransomNote[i] == magazine[j]):
                i += 1
                j += 1
            else:
                j += 1
        return i == len(ransomNote)

    # Runtime 16 ms / Memory 13.5 MB    
    def canConstruct_2(self, ransomNote, magazine):
        for c in ransomNote:
            if c not in magazine:
                return False
            magazine = magazine.replace(c, '', 1) # or use hash_map 
        return True