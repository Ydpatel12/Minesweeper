
import random

class Minesweeper:
    def __init__(self, rows, cols, mines):
        self.rows = rows
        self.cols = cols
        self.total_mines = mines
        self.board = [['' for _ in range(cols)] for _ in range(rows)]
        self.revealed = [[False for _ in range(cols)] for _ in range(rows)]
        self.game_over = False
        self.win = False
        self._place_mines()
        self._calculate_numbers()
        
    def _place_mines(self):
        positions = [(r, c) for r in range(self.rows) for c in range(self.cols)]
        for r, c in random.sample(positions, self.total_mines):
            self.board[r][c] = 'M'
            
            
    def _calculate_numbers(self):
        for r in range(self.rows):
            for c in range(self.cols):
                if self.board[r][c] == 'M':
                    continue
                count = 0
                for dr in [-1, 0, 1]:
                    for dc in [-1, 0, 1]:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < self.rows and 0 <= nc < self.cols and self.board[nr][nc] == 'M':
                            count += 1
                self.board[r][c] = str(count) if count > 0 else ''
                
                
    def reveal(self, r, c):
        if self.revealed[r][c] or self.game_over:
            return
        self.revealed[r][c] = True
        if self.board[r][c] == 'M':
            self.game_over = True
        elif self.board[r][c] == '':
            for dr in [-1, 0, 1]:
                for dc in [-1, 0, 1]:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < self.rows and 0 <= nc < self.cols:
                        self.reveal(nr, nc)
        self._check_win()

    def _check_win(self):
        for r in range(self.rows):
            for c in range(self.cols):
                if self.board[r][c] != 'M' and not self.revealed[r][c]:
                    return
        self.win = True
        self.game_over = True
        
        
    def to_dict(self):
        return {
            'rows': self.rows,
            'cols': self.cols,
            'mines': self.total_mines,
            'board': self.board,
            'revealed': self.revealed,
            'game_over': self.game_over,
            'win': self.win
        }
        
        
    @classmethod
    def from_dict(cls, data):
        game = cls(data['rows'], data['cols'], data['mines'])
        game.board = data['board']
        game.revealed = data['revealed']
        game.game_over = data['game_over']
        game.win = data['win']
        return game

