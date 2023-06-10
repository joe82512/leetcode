# -*- coding: utf-8 -*-
class Solution(object):
    # Runtime 31 ms / Memory 13.5 MB
    def flipAndInvertImage_1(self, image):
        result = []
        for stack in image:
            s = []
            while (stack):
                s.append(1-stack.pop())
            result.append(s)
        return result

    # Runtime 27 ms / Memory 13.4 MB
    def flipAndInvertImage_2(self, image):
        n = len(image)
        for i in range(n):
            for j in range(n//2):
                (image[i][j], image[i][n-j-1]) = (1-image[i][n-j-1], 1-image[i][j])
            if (n%2==1):
                image[i][n//2] = 1-image[i][n//2]
        return image