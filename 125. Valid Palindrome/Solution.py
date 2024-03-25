class Solution(object):
    # Runtime 32 ms / Memory 13.8 MB
    def isPalindrome_1(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left, right = 0, len(s) - 1

        while left < right:
            c_left = s[left]
            c_right = s[right]

            if not c_left.isalnum():
                left += 1
            elif not c_right.isalnum():
                right -= 1
            elif c_left.lower() != c_right.lower():
                return False
            else:
                left += 1
                right -= 1

        return True
    
    # Runtime 16 ms / Memory 13.7 MB
    def isPalindrome_2(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = [i for i in s.lower() if i.isalnum()]
        return s==s[::-1]