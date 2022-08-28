# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    # Runtime 33 ms / Memory 13.1 MB
    def firstBadVersion_1(self, n):
        left, right = 1, n
        while left < right:
            mid = left + (right - left) // 2
            if isBadVersion(mid):
                right = mid
            else:
                left = mid + 1
        return left
    # ref: https://ithelp.ithome.com.tw/articles/10243876

    # Runtime 24 ms / Memory 13.1 MB
    def firstBadVersion_2(self, n):
        if n == 1:
            return n
        else:
            left, right = 1, n
            while left < right:
                mid = (left + right)//2
                if mid == left: # B.C : mid == left == right-1
                    if isBadVersion(left):
                        return left
                    else:
                        return right
                else:
                    if isBadVersion(mid): # change B.C
                        right = mid
                    else:
                        left = mid



if __name__ == '__main__':
    print("=====================================")   