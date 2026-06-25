class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        r=len(matrix)
        c=len(matrix[0])
        for i in range(r):
            for j in range(c):
                if matrix[i][j]==0:
                    self.markinf(matrix,i,j)
        for i in range(r):
            for j in range(c):
                if matrix[i][j]==float('inf'):
                    matrix[i][j]=0
        
    def markinf(self,matrix,r,c):
        row=len(matrix)
        col=len(matrix[0])
        for i in range(0,row):
            if matrix[i][c]!=0:
                matrix[i][c]=float('inf')
        for j in range(0,col):
            if matrix[r][j]!=0:
                matrix[r][j]=float('inf')