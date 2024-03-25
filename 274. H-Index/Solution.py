class Solution(object):
    # Runtime 23 ms / Memory 11.9 MB
    def hIndex_1(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        # H-index: 評估論文發表品質, 有 H 篇文章至少被引用 H 次
        # ref: http://tul.blog.ntu.edu.tw/archives/2485
        
        # 倒序
        citations.sort()
        citations.reverse()
        # search
        for i,c in enumerate(citations):
            if (i>=c):
                return i
        # not found
        return len(citations)
    
    # Runtime 22 ms / Memory 11.7 MB
    def hIndex_2(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        # H-index: 評估論文發表品質, 有 H 篇文章至少被引用 H 次
        # ref: http://tul.blog.ntu.edu.tw/archives/2485
        
        # 正序
        citations.sort()
        # search
        total_c = len(citations)
        for i,c in enumerate(citations):
            if ( c >= total_c-i):
                return total_c-i
        # else
        return 0