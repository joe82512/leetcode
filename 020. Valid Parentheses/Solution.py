class Solution(object):
    # Runtime 15 ms / Memory 13.7 MB
    def isValid_1(self, s):
        stack = []
        parentheses = {
            '(':')',
            '[':']',
            '{':'}'
        }

        for c in s:
            if c in parentheses:
                stack.append(parentheses[c])
                #print('in :',stack)
            elif not stack or stack[-1]!=c:
                return False
            else:
                stack.pop()
                #print('out :',stack)

        return len(stack)==0

    # Runtime ms / Memory MB
    def isValid_2(self, s):
        pass