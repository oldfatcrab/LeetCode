class Solution:
    def isValid(self, colInd, cols):
        for i in range(len(cols)):
            if cols[i] == colInd:
                return False
            if i + cols[i] == len(cols) + colInd:
                return False
            if i - cols[i] == len(cols) - colInd:
                return False
        return True
    
    def dfs(self, n, cols):
        if len(cols) == n:
            self.ans += 1
        for i in range(n):
            if not self.isValid(i, cols):
                continue
            cols.append(i)
            self.dfs(n, cols)
            cols.pop()
                
    def totalNQueens(self, n):
        # write your code here
        self.ans = 0
        if n is None or n <= 0:
            return self.ans
        self.dfs(n, [])
        return self.ans