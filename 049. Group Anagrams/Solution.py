# -*- coding: utf-8 -*-
class Solution(object):
    # Runtime 223 ms / Memory 17.7 MB
    def groupAnagrams_1(self, strs):
        group = {}
        for string in strs:            
            sort_str = sorted([s for s in string])
            sort_str = "".join(sort_str)
            if not sort_str in group:
                group[sort_str] = []
            group[sort_str].append(string)                
        return list(group.values())

    # Runtime ms / Memory MB    
    def groupAnagrams_2(self, strs):
        pass



if __name__ == '__main__':
    print(Solution().groupAnagrams_1(["eat","tea","tan","ate","nat","bat"]))
    print(Solution().groupAnagrams_1([""]))
    print(Solution().groupAnagrams_1(["a"]))
    print("=====================================")