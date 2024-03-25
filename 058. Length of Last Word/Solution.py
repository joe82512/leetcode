class Solution(object):
    # Runtime 11 ms / Memory 11.8 MB
    def lengthOfLastWord_1(self, s):
        """
        :type s: str
        :rtype: int
        """
        temp_len = 0
        idx = len(s)-1
        # backend to word
        while (idx>=0) and (s[idx]==' '):
            idx = idx - 1
        # calculate word length
        while (idx>=0) and (s[idx]!=' '):
            idx = idx - 1
            temp_len = temp_len + 1
        # result
        return temp_len
    
    # Runtime 12 ms / Memory 12 MB
    def lengthOfLastWord_2(self, s):
        """
        :type s: str
        :rtype: int
        """
        s_list = s.split()
        return len(s_list[-1])