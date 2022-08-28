# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    # Runtime 50 ms / Memory 16.1 MB
    def levelOrder_1(self, root):
        queue = [root]
        result = []
            
        while queue:
            level = []
            
            for i in range(len(queue)):
                node = queue.pop(0) #remove first
                if node:
                    level.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)

            if level:
                result.append(level)
            
        return result

    # Runtime 22 ms / Memory 14.5 MB
    def levelOrder_2(self, root):
        self.level_order_traversal = [] #initial
        if root is None:
            return None
        else:
            self.level_order_traversal.append([root.val]) #get first node
            self.level_order(root)
            return self.level_order_traversal
    
    def level_order(self, root, level_number=0):
        if root is None:
            return None

        else:
            self.level_order_traversal.append([]) #append level_order_traversal
            level_number += 1

            #change level_order_traversal
            if root.left:
                self.level_order_traversal[level_number].append(root.left.val)
            if root.right:
                self.level_order_traversal[level_number].append(root.right.val)

            self.level_order(root.left, level_number=level_number) #Loop
            self.level_order(root.right, level_number=level_number)

            if self.level_order_traversal[-1] == []:
                self.level_order_traversal.pop() #goto bottom, remove



if __name__ == '__main__':
    print("=====================================")   