# -*- coding: utf-8 -*-
class Solution(object):
    # Runtime 99 ms / Memory 13.3 MB
    def combinationSum_1(self, candidates, target):
        res_list = []
        self.comb(candidates,target,[],res_list)
        return res_list
        
    def comb(self,can,tar,res,res_list):
        if tar == 0:
            res_list.append(res)
            return None
        elif tar > 0:
            for i in range(len(can)):
                self.comb(can[i:], tar-can[i], res+[can[i]], res_list)
        else:
            return None

    # Runtime ms / Memory MB
    def combinationSum_2(self, candidates, target):
        pass