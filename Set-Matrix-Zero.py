class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        row = list(len(matrix)*'0')
        col = list(len(matrix[0])*'0')
        print(len(row), len(col))
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]==0:
                    print(i, j)
                    row[i] = 1
                    col[j] = 1
        for i in range(len(row)):
            for j in range(len(col)):
                if row[i]==1 or col[j]==1:
                    matrix[i][j] = 0
        print(row, col)
