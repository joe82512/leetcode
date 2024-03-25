class Solution(object):
    # Runtime 79 ms / Memory 12.8 MB
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        row, col = len(matrix), len(matrix[0])
        zeros = []
        # scan all
        for i in range(row):
            for j in range(col):
                if (matrix[i][j]==0):
                    zeros.append((i,j))

        # replace after scan
        for (i,j) in zeros:
            for c in range(col):
                matrix[i][c] = 0
            for r in range(row):
                matrix[r][j] = 0

    # Runtime 92 ms / Memory 12.6 MB
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        row, col = len(matrix), len(matrix[0])
        zeros_row = [False]*row
        zeros_col = [False]*col

        # scan all
        for i in range(row):
            for j in range(col):
                if (matrix[i][j]==0):
                    zeros_row[i] = True
                    zeros_col[j] = True

        # replace after scan
        for i in range(row):
            for j in range(col):
                if (zeros_row[i]):
                    matrix[i][j] = 0
                elif (zeros_col[j]):
                    matrix[i][j] = 0