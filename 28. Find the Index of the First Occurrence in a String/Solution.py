class Solution(object):
    # Runtime 10 ms / Memory 11.7 MB
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if len(haystack) < len(needle) :
            return -1
        elif (haystack == needle):
            return 0
        #else: sliding window
        h_l, n_l = len(haystack), len(needle)

        for L in range(h_l-n_l+1):
            for W in range(n_l):
                if (haystack[L+W] != needle[W]):
                    break
                elif (W == n_l-1): #go through
                    return L

        return -1
    
    # Runtime 16 ms / Memory 11.8 MB
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        return haystack.find(needle)
        