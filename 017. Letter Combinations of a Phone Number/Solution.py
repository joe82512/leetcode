# -*- coding: utf-8 -*-
class Solution:
    # Runtime 27 ms / Memory 13.6 MB
    def letterCombinations_1(self, digits):
        num_dic = {
            '2':('a','b','c'),
            '3':('d','e','f'),
            '4':('g','h','i'),
            '5':('j','k','l'),
            '6':('m','n','o'),
            '7':('p','q','r','s'),
            '8':('t','u','v'),
            '9':('w','x','y','z'),
        }        
        if digits == "":
            return []
        else:
            str_list = [""]
            for s in digits:
                str_list = [sl+add_str for add_str in num_dic[s] for sl in str_list]
                '''
                temp_list = []
                for add_str in num_dic[s]:
                    for sl in str_list:
                        temp_list.append(sl+add_str)
                str_list = temp_list
                '''                
            return str_list

    # Runtime 24 ms / Memory 13.4 MB    
    def letterCombinations_2(self, digits):
        self.words = {'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        self.digits = digits
        
        if len(digits)==0:
            return []
        else:
            res=[]
            self.dfs(0,[],res)
            return res
        
    def dfs(self,nums,path,res):
        if nums==len(self.digits):
            res.append(''.join(path))
            # print(path)
            return
        else:
            next_number = self.digits[nums]
            for word in self.words[next_number]:
                path.append(word)
                self.dfs(nums+1,path,res)
                path.pop()



if __name__ == '__main__':
    print(Solution().letterCombinations_1("23"))
    print(Solution().letterCombinations_1(""))
    print(Solution().letterCombinations_1("2"))
    print("=====================================")
    print(Solution().letterCombinations_2("23"))
    print(Solution().letterCombinations_2(""))
    print(Solution().letterCombinations_2("2"))   