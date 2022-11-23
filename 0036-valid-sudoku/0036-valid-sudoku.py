class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool: 
        return (self.is_row(board) and self.is_column(board) and self.is_square(board))
    
    def is_row(self,board):
        for row in board:
            if not self.is_everything_ok(row):
                return False
        return True
        
    def is_column(self,board):
        for column in zip(*board):
            if not self.is_everything_ok(column):
                return False
        return True
        
    def is_square(self,board):
        for i in (0,3,6):
            for j in (0,3,6):
                square = []
                for m in range(i,i+3):
                    for n in range(j,j+3):
                        square.append(board[m][n])
                if not self.is_everything_ok(square):
                    return False
        return True
        
    def is_everything_ok(self,check):
        check_ = []
        for i in check:
            if i!='.':
                check_.append(i)
        return len(check_)==len(set(check_))