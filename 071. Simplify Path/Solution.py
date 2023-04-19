# -*- coding: utf-8 -*-
class Solution(object):
    # Runtime 26 ms / Memory 13.6 MB
    def simplifyPath_1(self, path):
        subpath = path.split('/')
        stack = []
        for sb in subpath:
            if sb=="" or sb==".":
                continue
            #else:
            if sb==".." and stack:
                stack.pop()
            elif sb!="..":
                stack.append(sb)
        return '/' + '/'.join(stack)

    # Runtime 38 ms / Memory 13.9 MB
    def simplifyPath_2(self, path):
        stack = []
        i = 0
        while (i < len(path)):
            sb = ""
            while (i<len(path) and path[i]!="/"):
                sb += path[i]
                i += 1
            
            if sb == "..":
                if stack:
                    stack.pop()
            elif (sb and sb != "."):
                stack.append(sb)
            i += 1
        
        new_path = ""
        while stack:
            new_path = '/' + stack.pop() + new_path
            
        if not new_path:
            return "/"
        else:
            return new_path