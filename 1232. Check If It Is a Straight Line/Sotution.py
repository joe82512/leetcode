# -*- coding: utf-8 -*-
class Solution(object):
    # Runtime 45 ms / Memory 13.7 MB
    def checkStraightLine(self, coordinates):
        n = len(coordinates)
        if n <= 2:
            return True

        c0 = coordinates.pop(0)
        c1 = coordinates.pop(0)
        (dx,dy) = ( (c1[0]-c0[0]) , (c1[1]-c0[1]) )

        for c in coordinates:
            if dx*(c[1]-c1[1]) != dy*(c[0]-c1[0]):
                return False

        return True