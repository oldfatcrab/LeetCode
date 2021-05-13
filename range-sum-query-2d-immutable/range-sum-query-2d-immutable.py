class NumMatrix:
    
    def __init__(self, matrix: List[List[int]]):
        numRow, numCol = len(matrix), len(matrix[0])
        self.A = [[0] * (numCol + 1) for _ in range(numRow + 1)]
        for i in range(numRow):
            for j in range(numCol):
                self.A[i + 1][j + 1] = self.A[i + 1][j] + self.A[i][j + 1] - self.A[i][j] + matrix[i][j] 
                
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.A[row2 + 1][col2 + 1] - self.A[row1][col2 + 1] - self.A[row2 + 1][col1] + self.A[row1][col1]
