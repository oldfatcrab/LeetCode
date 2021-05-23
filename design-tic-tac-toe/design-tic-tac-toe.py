from collections import defaultdict

class TicTacToe:

    def __init__(self, n: int):
        """
        Initialize your data structure here.
        """
        self.board = defaultdict(int)
        self.n = n

    def move(self, row: int, col: int, player: int) -> int:
        self.board[(row, col)] = player
        isRow, isCol, isSlash, isBackslash = True, True, False, False
        for i in range(self.n):
            isCol = isCol and (self.board[(row, i)] == player)
            
        for i in range(self.n):
            isRow = isRow and (self.board[(i, col)] == player)
                
        if row == col:
            isBackslash = True
            for i in range(self.n):
                isBackslash = isBackslash and (self.board[(i, i)] == player)
                    
        if row + col == self.n - 1:
            isSlash = True
            for i in range(self.n):
                isSlash = isSlash and (self.board[(i, self.n - 1 - i)] == player)
        return player if (isRow or isCol or isSlash or isBackslash) else 0
                
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        """
        
        


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)